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
compressed TSV exports of tables using a command `WbExport`:

```
WbExport -type=text -compress
-file='C:\Users\nmartinsenburrell\documents\notes.tsv'
-sourceTable='II_GA_NOTES'
-schema='NRM_GA';
```

The Oracle PL/SQL Developer is available in NRM's Citrix environment and can
also create TSV exports by running the SQL command `SELECT * FROM
NRM_GA.II_GA_NOTES` and then clicking on the `Export Query Results...` button
and selecting `TSV`.

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

Get the edited DDL script and TSV data file onto a computer that has access
to cloud.gov and the `connect-to-service` Cloudflare plugin. Run `cf
connect-to-service APP_NAME SERVICE_NAME` to get a `psql` session connected to
the Postgres database. Create the table by running the SQL script:

```
\i notes.create.sql
```

and then import the data with

```
\copy ii_ga_notes FROM 'notes_no_header.tsv' WITH (FORMAT TEXT);
```

## DDL files

DDL scripts for some of the tables that we've converted are here in this
directory as examples of how to make Postgres-compatible versions of Oracle
tables.  These aren't guaranteed to be up-to-date as we improve the fidelity
of our processes for importing matching data structures, but we intend them to
be good examples.
