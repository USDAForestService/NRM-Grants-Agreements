# Generated by Django 3.2.4 on 2021-07-01 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("grants", "0009_auto_20210329_1606"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "cn",
                    models.CharField(max_length=34, primary_key=True, serialize=False),
                ),
                ("category_cd", models.CharField(max_length=2, verbose_name="Code")),
                (
                    "category_desc",
                    models.CharField(
                        blank=True,
                        max_length=120,
                        null=True,
                        verbose_name="Description",
                    ),
                ),
                ("last_update", models.DateField(auto_now=True)),
            ],
            options={
                "db_table": "ii_ga_ip_categories",
            },
        ),
        migrations.AlterModelOptions(
            name="grant",
            options={
                "ordering": ["-created_date"],
                "verbose_name": "Grant/Agreement",
                "verbose_name_plural": "Grants and Agreements",
            },
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
                default="Other",
                help_text="\n            Applies to instruments with Federal Financial Assistance (FFA).\n            Select OTHER if not FFA.\n        ",
                max_length=100,
                verbose_name="Type of Submission",
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="app_submit_date",
            field=models.DateField(
                help_text="The date the proposal was submitted for review or processing.",
                verbose_name="Application submitted",
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="application_type",
            field=models.CharField(
                choices=[
                    ("NEW", "New"),
                    ("CONTINUATION", "Continuation"),
                    ("REVISION A-INCREASE AWARD", "Revision A - Increase Award"),
                    ("REVISION B-DECREASE AWARD", "Revision B - Decrease Award"),
                    ("REVISION C-INCREASE AWARD", "Revision C - Increase Duration"),
                    ("REVISION D-DECREASE AWARD", "Revision D - Decrease Duration"),
                    ("OTHER", "Other"),
                ],
                default="Other",
                help_text="\n            Applies to instruments with Federal Financial Assistance (FFA).\n            Select OTHER if not FFA.\n        ",
                max_length=30,
                verbose_name="Type of application",
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="cooperator_agreement_number",
            field=models.CharField(
                blank=True,
                help_text="Cooperator's agreement number, if different than the Forest Service Agreement Number",
                max_length=34,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="progrm_responsibility_type",
            field=models.CharField(
                choices=[
                    ("INCOMING FUNDING AGREEMENT", "Incoming funding agreement"),
                    ("NON-CASH AGREEMENT", "Non-cash agreement"),
                    ("OUTGOING FUNDING AGREEMENT", "Outgoing funding agreement"),
                ],
                help_text="\n            Indicates the specific responsibilities notification type\n            (Incoming Funding, Outgoing Funding, or Non-Cash ie no exchange of funding)\n            that is send to the Program Manager when the agreement is executed.\n        ",
                max_length=30,
                null=True,
                verbose_name="Program Responsibility Type",
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="proj_title",
            field=models.CharField(
                db_index=True,
                help_text="The short and concise name of the project. Do not include any acronyms, unit codes, or funding codes.",
                max_length=200,
                verbose_name="Project title",
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="state_eo_date",
            field=models.DateField(
                blank=True,
                help_text="\n            Executive Order 12372 review date.\n            You must select a date if 'Subject to State E.O.' is Yes.",
                null=True,
                verbose_name="EO Date",
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="status",
            field=models.CharField(
                choices=[
                    ("AGREEMENT-ACTION", "Agreement action"),
                    ("NEW-APPLICATION", "New application"),
                    ("APP-ACCEPTED", "App accepted"),
                    ("APP-APPROVED", "App approved"),
                    ("APP-PGM REJECTED", "App PGM rejected"),
                    ("APP-RECEIVED", "App received"),
                    ("APP-REJECTED", "App rejected"),
                    ("GA-CANCELLED", "GA closed"),
                    ("GA-EXECUTED", "GA executed"),
                    ("GA-PENDING", "GA pending"),
                    ("GA-TERMINATED", "GA terminated"),
                ],
                default="NEW-APPLICATION",
                editable=False,
                max_length=40,
                verbose_name="Agreement Status",
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="status_date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="grant",
            name="wppp_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Awaiting Documentation", "Awaiting Documentation"),
                    ("Executed- Active", "Executed - Active"),
                    ("G&A Closed", "G&A Closed"),
                    ("G&A Closeout in process", "G&A Closeout in process"),
                    ("G&A Reviewing", "G&A Reviewing"),
                    ("New", "New"),
                    ("Out for Signature", "Out for Signature"),
                    ("Pending ASC Action", "Pending ASC Action"),
                ],
                editable=False,
                max_length=40,
                null=True,
                verbose_name="WPAP Status",
            ),
        ),
        migrations.AlterField(
            model_name="grant",
            name="wppp_status_date",
            field=models.DateField(
                blank=True, editable=False, null=True, verbose_name="WPAP status date"
            ),
        ),
        migrations.AddConstraint(
            model_name="grant",
            constraint=models.UniqueConstraint(fields=("gid",), name="unique_gid"),
        ),
        migrations.AddField(
            model_name="category",
            name="grant",
            field=models.ForeignKey(
                db_column="grant_cn",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="grants.grant",
            ),
        ),
    ]
