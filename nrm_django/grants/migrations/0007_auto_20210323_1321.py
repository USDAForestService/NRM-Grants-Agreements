# Generated by Django 3.1.7 on 2021-03-23 13:21
# Saved to let Black reformat and stop complaining.

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("grants", "0006_note_grant_foreignkey"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="grant",
            options={
                "verbose_name": "Grant/Agreement",
                "verbose_name_plural": "Grants and Agreements",
            },
        ),
        migrations.RemoveField(
            model_name="grantauthority",
            name="grant_cn",
        ),
        migrations.AddField(
            model_name="grantauthority",
            name="grant",
            field=models.ForeignKey(
                db_column="grant_cn",
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="grants.grant",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="grantauthority",
            name="id",
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="grant",
            name="advance_allowed_ind",
            field=models.CharField(
                choices=[("Y", "Yes"), ("N", "No")],
                default="N",
                max_length=1,
                null=True,
                verbose_name="Advance Allowed",
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="app_submission_type",
            field=models.CharField(
                choices=[
                    ("NEW", "New"),
                    ("Application", "Application"),
                    ("Preapplication", "Pre-application"),
                    (
                        "NON-CONSTRUCTION PRE-APPLICATION",
                        "Non-construction Pre-application",
                    ),
                    ("NON-CONSTRUCTION APPLICATION", "Non-construction Application"),
                    ("CONSTRUCTION PRE-APPLICATION", "Construction Pre-application"),
                    ("CONSTRUCTION APPLICATION", "Construction Application"),
                    ("MOU", "Mou"),
                    ("OTHER", "Other"),
                    (
                        "8/1/2004NON-CONSTRUCTION APPLICATION",
                        "8/1/2004NON-CONSTRUCTION APPLICATION",
                    ),
                    (
                        "5/1/2005NON-CONSTRUCTION APPLICATION",
                        "5/1/2005NON-CONSTRUCTION APPLICATION",
                    ),
                ],
                max_length=100,
                verbose_name="Application submission type",
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="applicant_name",
            field=models.CharField(
                blank=True,
                max_length=200,
                null=True,
                verbose_name="Applicant/Cooperator Name",
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="application_id",
            field=models.CharField(editable=False, max_length=34),
        ),
        migrations.AlterField(
            model_name="grant",
            name="application_type",
            field=models.CharField(
                choices=[
                    ("Initial", "Initial"),
                    ("CONTINUATION", "Continuation"),
                    ("NEW", "New"),
                    ("OTHER", "Other"),
                    ("REVISION A-INCREASE AWARD", "Revision A - Increase Award"),
                    ("REVISION C-INCREASE AWARD", "Revision C - Increase Duration"),
                ],
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="authority",
            field=models.CharField(
                blank=True,
                choices=[("Y", "Yes"), ("N", "No")],
                default="N",
                max_length=1,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="authority_approval",
            field=models.CharField(
                blank=True,
                choices=[("Y", "Yes"), ("N", "No")],
                default="N",
                max_length=1,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="cn",
            field=models.CharField(
                db_index=True,
                editable=False,
                max_length=34,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="created_by",
            field=models.CharField(editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name="grant",
            name="created_date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="grant",
            name="created_in_instance",
            field=models.DecimalField(decimal_places=0, editable=False, max_digits=6),
        ),
        migrations.AlterField(
            model_name="grant",
            name="fed_id_fy",
            field=models.CharField(
                blank=True,
                choices=[
                    ("2021", "2021"),
                    ("2020", "2020"),
                    ("2019", "2019"),
                    ("2018", "2018"),
                    ("2017", "2017"),
                    ("2016", "2016"),
                    ("2015", "2015"),
                    ("2014", "2014"),
                    ("2013", "2013"),
                    ("2012", "2012"),
                    ("2011", "2011"),
                    ("2010", "2010"),
                    ("2009", "2009"),
                    ("2008", "2008"),
                    ("2007", "2007"),
                    ("2006", "2006"),
                    ("2005", "2005"),
                    ("2004", "2004"),
                    ("2003", "2003"),
                    ("2002", "2002"),
                    ("2001", "2001"),
                    ("2000", "2000"),
                    ("1999", "1999"),
                    ("1998", "1998"),
                    ("1997", "1997"),
                    ("1996", "1996"),
                    ("1995", "1995"),
                    ("1994", "1994"),
                    ("1993", "1993"),
                    ("1992", "1992"),
                    ("1991", "1991"),
                    ("1990", "1990"),
                    ("1989", "1989"),
                    ("1988", "1988"),
                    ("1987", "1987"),
                    ("1986", "1986"),
                    ("1985", "1985"),
                    ("1984", "1984"),
                    ("1983", "1983"),
                    ("1982", "1982"),
                    ("1981", "1981"),
                    ("1980", "1980"),
                    ("1979", "1979"),
                    ("1978", "1978"),
                    ("1977", "1977"),
                    ("1976", "1976"),
                    ("1975", "1975"),
                    ("1974", "1974"),
                    ("1973", "1973"),
                    ("1972", "1972"),
                    ("1971", "1971"),
                    ("1970", "1970"),
                    ("1969", "1969"),
                    ("1968", "1968"),
                    ("1967", "1967"),
                    ("1966", "1966"),
                    ("1965", "1965"),
                    ("1964", "1964"),
                    ("1963", "1963"),
                    ("1962", "1962"),
                    ("1961", "1961"),
                    ("1960", "1960"),
                    ("1959", "1959"),
                    ("1958", "1958"),
                    ("1957", "1957"),
                    ("1956", "1956"),
                    ("1955", "1955"),
                    ("1954", "1954"),
                    ("1953", "1953"),
                    ("1952", "1952"),
                    ("1951", "1951"),
                    ("1950", "1950"),
                    ("1949", "1949"),
                ],
                max_length=4,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="fed_id_region",
            field=models.CharField(
                blank=True,
                choices=[
                    (" ", " "),
                    ("01", "01"),
                    ("02", "02"),
                    ("03", "03"),
                    ("04", "04"),
                    ("05", "05"),
                    ("06", "06"),
                    ("07", "07"),
                    ("08", "08"),
                    ("09", "09"),
                    ("10", "10"),
                    ("11", "11"),
                    ("12", "12"),
                    ("13", "13"),
                    ("15", "15"),
                    ("16", "16"),
                    ("22", "22"),
                    ("23", "23"),
                    ("24", "24"),
                    ("25", "25"),
                    ("26", "26"),
                    ("27", "27"),
                    ("33", "33"),
                    ("42", "42"),
                ],
                max_length=2,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="fed_id_type",
            field=models.CharField(
                blank=True,
                choices=[
                    (" ", " "),
                    ("CA", "CA"),
                    ("CO", "CO"),
                    ("CR", "CR"),
                    ("CS", "CS"),
                    ("DG", "DG"),
                    ("DP", "DP"),
                    ("FA", "FA"),
                    ("FI", "FI"),
                    ("FO", "FO"),
                    ("FP", "FP"),
                    ("GN", "GN"),
                    ("IA", "IA"),
                    ("IC", "IC"),
                    ("IG", "IG"),
                    ("IJ", "IJ"),
                    ("JV", "JV"),
                    ("LE", "LE"),
                    ("LI", "LI"),
                    ("MU", "MU"),
                    ("OR", "OR"),
                    ("PA", "PA"),
                    ("RD", "RD"),
                    ("RO", "RO"),
                    ("RU", "RU"),
                    ("SA", "SA"),
                    ("SU", "SU"),
                    ("TR", "TR"),
                ],
                max_length=2,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="format",
            field=models.CharField(
                blank=True,
                choices=[("Y", "Yes"), ("N", "No")],
                default="N",
                max_length=1,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="gid",
            field=models.CharField(
                blank=True, max_length=16, null=True, verbose_name="Agreement Number"
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="hhs_payment_ind",
            field=models.CharField(default="N", editable=False, max_length=1),
        ),
        migrations.AlterField(
            model_name="grant",
            name="international_act_ind",
            field=models.CharField(
                choices=[("Y", "Yes"), ("N", "No")],
                default="N",
                max_length=1,
                null=True,
                verbose_name="International Act",
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="last_update",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="grant",
            name="locked_ind",
            field=models.CharField(
                choices=[("Y", "Yes"), ("N", "No")],
                default="N",
                editable=False,
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="master_fed_id",
            field=models.CharField(
                blank=True, max_length=120, null=True, verbose_name="Master Fed ID"
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="modified_date",
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="grant",
            name="modified_in_instance",
            field=models.DecimalField(
                blank=True, decimal_places=0, editable=False, max_digits=6, null=True
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="orig_fed_id",
            field=models.CharField(
                blank=True, max_length=120, null=True, verbose_name="Original Fed ID"
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="other_approval",
            field=models.CharField(
                blank=True,
                choices=[("Y", "Yes"), ("N", "No")],
                default="N",
                max_length=1,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="proj_expiration_dt",
            field=models.DateField(blank=True, null=True, verbose_name="Expires"),
        ),
        migrations.AlterField(
            model_name="grant",
            name="proj_start_dt",
            field=models.DateField(blank=True, null=True, verbose_name="Start date"),
        ),
        migrations.AlterField(
            model_name="grant",
            name="proj_status",
            field=models.CharField(
                blank=True,
                choices=[("", "----"), ("01", "01"), ("02", "02")],
                max_length=15,
                null=True,
                verbose_name="Project status",
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="proj_title",
            field=models.CharField(
                db_index=True, max_length=200, verbose_name="Project title"
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="proj_type",
            field=models.CharField(
                blank=True,
                choices=[("", "----"), ("01", "01"), ("02", "02")],
                max_length=3,
                null=True,
                verbose_name="Project Type",
            ),
        ),
        migrations.AlterField(
            model_name="note",
            name="cn",
            field=models.CharField(
                db_index=True, max_length=34, primary_key=True, serialize=False
            ),
        ),
    ]
