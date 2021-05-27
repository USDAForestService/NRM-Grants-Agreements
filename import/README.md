# Importing data from Oracle to Postgres

We would like to use PostgreSQL on cloud.gov for our rapid prototyping work on
the NRM G&A application. The current production data is in NRM's Oracle
database, so we need to copy data with the correct structure from Oracle and
import it into our Postgres database. This is complicated by the Oracle server
only being accessible on NRM's VPN. Here is what works for us, kind of.

## Export from Oracle as TSV

Using a SQL client, export a single G&A table as a TSV file. 

The open-source (SQLWorkbench/J)[https://www.sql-workbench.eu/] is java-based
and can be run most anywhere, on GSA and Forest Service laptops. It can create
compressed TSV exports of tables using a command `WbExport` (change the path
of the file to match your user and operating system):

```
WbExport -type=text -compress
-file='C:\Users\nmartinsenburrell\documents\notes.tsv'
-sourceTable='II_GA_NOTES'
-schema='NRM_GA';
```

The Oracle PL/SQL Developer application is available in NRM's Citrix
environment and can also create TSV exports by running the SQL command `SELECT
* FROM NRM_GA.II_GA_NOTES` and then clicking on the `Export Query Results...`
button and selecting `TSV`.

## Export a DDL for the Oracle Table

In order to load the exported TSV data, we need to be able to create a table
in Postgres that has the matching structure, with the same fields and
(roughly) the same data types. In SQLWorkbench/J, open the Database Explorer,
select the table, right-click and select "Create DDL Script", then save the
result as a file with a `.sql` extension such as `notes.create.sql`.

## Modify the DDL for Postgres

The data types present in an Oracle table have a rough correspondence with
those in Postgres, but not exact. Here are some of the changes that you might
have to make.

- Replace `VARCHAR2` with `VARCHAR`
- Replace `NUMBER` with `NUMERIC`
- Remove ` Bytes` from Oracle's `VARCHAR(32 Bytes)`
- Remove a schema name (if the table will be created in a different schema)
- Remove or update `TABLESPACES` and `INDEXES`

## Import the data into Postgres

The Postgres `\copy` command expects TSV files without a header line (that
lists the column names) but both export methods described above include a
header. Remove the first line of the file

```
tail -n +2 notes.tsv > notes_no_header.tsv
```

Get the edited DDL script and TSV data file onto a computer that has access to
cloud.gov and the `connect-to-service` (CloudFoundry
plugin)[https://github.com/cloud-gov/cf-service-connect]. Run `cf
connect-to-service fs-nrm fs-nrm-db` to get a `psql` session connected to the
Postgres database (where `fs-nrm` is the name of the Cloud.gov app and
`fs-nrm-db` is the name of the database service). Create the table by running
the SQL script inside of `psql`:

```
\i notes.create.sql
```

and then import the data with

```
\copy ii_ga_notes FROM 'notes_no_header.tsv' WITH (FORMAT TEXT);
```

Empty dates require special handling. Try using `(FORMAT TEXT, NULL '')` in
the above line if the first import doesn't work.

## DDL files

DDL scripts for some of the tables that we've converted are here in this
directory as examples of how to make Postgres-compatible versions of Oracle
tables.  These aren't guaranteed to be up-to-date as we improve the fidelity
of our processes for importing matching data structures, but we intend them to
be good examples.


## Using the imported data

Once you have the tables populated in the database, you can run Django's [inspectdb command](https://docs.djangoproject.com/en/3.1/ref/django-admin/#django-admin-inspectdb) to build a draft version of your models. A few things to note:

1. In most cases, `inspectdb` will not understand ForeignKeys and other relationships between tables. You will have to change those yourself, and you may need to migrate afterward.
2. In most cases `inspectdb` will specify `db_table` in the generated models' Meta information. When working with legacy databases, this is very helpful and allows you to rename the model to improve readability in the admin while using the original database table names. Similarly, verbose name option on individual fields can be useful for improving readability.
3. By default, inspectdb creates unmanaged models. That is, `managed = False` in the model’s Meta class tells Django not to manage each table’s creation, modification, and deletion. If you do want to allow Django to manage the table’s lifecycle, you’ll need to change the managed option to True (or remove it because True is its default value).

You can copy and paste the results of `inspectdb` into your models by hand, or, if you prefer,  output it straight to a file: `python manage.py inspectdb > models.py`.

When your models are created, you will also have to go through the usual Django steps of adding them to `INSTALLED_APPS` in the site settings and [making them editable in the admin](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin).


## Importing cleaned data

First, you'll need a JSON fixture. If the data has already been in a database, Django's `dumpdata` will create one for you.

You will need that file in hand on your local machine as well as an up-to-date copy of your `replacements.txt` file, if one has been created. Both of those should be in the `/import` folder. You'll then `cd` into the `/import` folder to run `python scrubber.py <fixture>`, with `<fixture>` being the name of your downloaded fixture.

See the scrubber.py file for more details.

That will output a new fixture with `_mod.json` at the end, as well as an updated (or new) `requirements.txt` file.

Loading your scrubbed fixture back into Django can be tricky. In theory you could upload it and then use Django's `loaddata` command to import it directly on cloud. However, we have found it more reliable to use the [cf-service-connect plugin](https://github.com/cloud-gov/cf-service-connect) to establish a long-running tunnel to Cloud, as outlined below. 

### Establishing a long-running shell to load data
1. If you haven't already, log in to cloud: `cf login -a api.fr.cloud.gov --sso`
2. Be sure you've targeted the correct space: `cf target -o <org name> -s <space name>`. You'll need to know your cloud org and space name.
3. Now connect: `cf connect-to-service -no-client <app name> <service name>`. If you get an error, you probably don't have the service-connect plugin installed, so back up and do that.

At this point, assuming you have no errors, service-connect will output new database connection parameters. You will need to either temporarily modify django settings or create a new `DATABASE_URL` environment variable to reflect these settings. Whichever route you go, don't make it too permanent: the next time you use service-connect they'll change.

Leave the service-connect terminal alone and open a new shell. From that new shell, with your temp settings in place, you should now be able to push data. Assuming you're in the `pipenv` shell inside `nrm_django`, that command would be `python manage.py loaddata ../import/<fixture>_mod.json --settings=nrm_site.settings.base --verbosity=3`

Note that you will need to pass the correct settings file to the manage.py command, as well as give it the path to the fixture you're trying to load. The `--verbosity=3` argument will provide some useful  progress feedback.

Note also that if you have existing DB rows in the table you may want to jump into a Django shell and run `<model>.objects.all().delete()` to remove them before loading your fixture.

### Backup and restore

Using the previous section, you can set up an SSH connection to the database
on cloud.gov. This lets us back up the database over that connection. Using
the username, password, and port from the `cf connect-to-service` command,
give those as arguments to the `pg_dump` command (you may need to install the
`postgresql` package of a matching major version to get that utility).

```
pg_dump -F c -h localhost -U <random_username> -p <random_port> <db_name> > backup.bin
```

`<db_name>` needs to be looked up separately using the `\l` command in `psql`.
The `-F c` option specifies the custom binary export format.

Once you have the backup file, you can restore it to any postgres database
that you have access to using the `pg_restore` utility.

```
pg_restore -h <new_host> -U <new_user> -p <new_port> -d ebdb backup.bin
```

where `ebdb` is the name of the database to use on the new host. (`ebdb` is
the default for Elastic Beanstalk.)
