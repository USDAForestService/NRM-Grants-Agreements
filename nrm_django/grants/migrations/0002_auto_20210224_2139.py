# Generated by Django 3.1.7 on 2021-02-24 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cn', models.CharField(max_length=34)),
                ('proj_title', models.CharField(max_length=200, verbose_name='Project title')),
                ('proj_status', models.CharField(blank=True, max_length=15, null=True, verbose_name='Project status')),
                ('application_id', models.CharField(max_length=34)),
                ('application_type', models.CharField(max_length=30)),
                ('app_submission_type', models.CharField(max_length=100, verbose_name='Application submission type')),
                ('app_submit_date', models.DateField(verbose_name='Application submitted')),
                ('app_received_date', models.DateField(verbose_name='Application received')),
                ('hhs_payment_ind', models.CharField(max_length=1)),
                ('proposed_start_date', models.DateField()),
                ('proposed_end_date', models.DateField()),
                ('locked_ind', models.CharField(max_length=1)),
                ('status', models.CharField(max_length=40)),
                ('status_date', models.DateField()),
                ('created_by', models.CharField(max_length=30)),
                ('created_date', models.DateField()),
                ('created_in_instance', models.DecimalField(decimal_places=0, max_digits=6)),
                ('modified_by', models.CharField(blank=True, max_length=30, null=True)),
                ('modified_date', models.DateField(blank=True, null=True)),
                ('modified_in_instance', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('fed_id_fy', models.CharField(blank=True, max_length=4, null=True)),
                ('fed_id_type', models.CharField(blank=True, max_length=2, null=True)),
                ('fed_id_agency', models.CharField(blank=True, max_length=2, null=True)),
                ('fed_id_region', models.CharField(blank=True, max_length=2, null=True)),
                ('fed_id_unit', models.CharField(blank=True, max_length=2, null=True)),
                ('fed_id_subunit', models.CharField(blank=True, max_length=2, null=True)),
                ('fed_id_seq', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('proj_desc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Project description')),
                ('proj_received_dt', models.DateField(blank=True, null=True, verbose_name='Project received date')),
                ('proj_execution_dt', models.DateField(blank=True, null=True, verbose_name='Project execution date')),
                ('proj_start_dt', models.DateField(blank=True, null=True, verbose_name='Project start date')),
                ('proj_obligation_dt', models.DateField(blank=True, null=True, verbose_name='Project obligation date')),
                ('proj_expiration_dt', models.DateField(blank=True, null=True, verbose_name='Project expiration date')),
                ('proj_rwu', models.CharField(blank=True, max_length=10, null=True)),
                ('proj_close_dt', models.DateField(blank=True, null=True, verbose_name='Project close date')),
                ('proj_cancellation_dt', models.DateField(blank=True, null=True, verbose_name='Project cancellation date')),
                ('proj_cfda_no', models.CharField(blank=True, max_length=40, null=True, verbose_name='Project CFDA')),
                ('proj_science_cd', models.CharField(blank=True, max_length=3, null=True)),
                ('project_congressional_district', models.CharField(blank=True, max_length=40, null=True)),
                ('date_mailed', models.DateField(blank=True, null=True)),
                ('date_signed', models.DateField(blank=True, null=True)),
                ('extramural_ind', models.CharField(blank=True, max_length=1, null=True)),
                ('research_type', models.CharField(blank=True, max_length=1, null=True)),
                ('journal_ind', models.CharField(blank=True, max_length=1, null=True)),
                ('mod_number', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('orig_fed_id', models.CharField(blank=True, max_length=120, null=True)),
                ('comments', models.CharField(blank=True, max_length=2000, null=True)),
                ('master_fed_id', models.CharField(blank=True, max_length=120, null=True)),
                ('aop_ind', models.CharField(blank=True, max_length=1, null=True)),
                ('geo_type', models.CharField(blank=True, max_length=2, null=True)),
                ('managing_state_county', models.CharField(blank=True, max_length=240, null=True)),
                ('areas_effected', models.CharField(blank=True, max_length=200, null=True)),
                ('ffin', models.CharField(blank=True, max_length=40, null=True)),
                ('state_identifier', models.CharField(blank=True, max_length=40, null=True)),
                ('state_eo_code', models.CharField(blank=True, max_length=1, null=True)),
                ('state_eo_date', models.DateField(blank=True, null=True)),
                ('fed_est_fund', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('applicant_est_fund', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('state_est_fund', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('local_est_fund', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('pi_est_fund', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('oth_est_fund', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('reroute_from', models.CharField(blank=True, max_length=10, null=True)),
                ('reroute_date', models.DateField(blank=True, null=True)),
                ('certificaion_date', models.DateField(blank=True, null=True)),
                ('ffis_doc_id', models.CharField(blank=True, max_length=11, null=True)),
                ('applicant_name', models.CharField(blank=True, max_length=200, null=True)),
                ('international_act_ind', models.CharField(blank=True, max_length=1, null=True)),
                ('proj_type', models.CharField(blank=True, max_length=3, null=True)),
                ('advance_allowed_ind', models.CharField(blank=True, max_length=1, null=True, verbose_name='Advance Allowed')),
                ('authority_approval', models.CharField(blank=True, max_length=1, null=True)),
                ('authority', models.CharField(blank=True, max_length=1, null=True)),
                ('format', models.CharField(blank=True, max_length=1, null=True)),
                ('other_approval', models.CharField(blank=True, max_length=1, null=True)),
                ('master_agreement_ind', models.CharField(blank=True, max_length=1, null=True)),
                ('progrm_responsibility_type', models.CharField(blank=True, max_length=30, null=True)),
                ('wppp_status', models.CharField(blank=True, max_length=40, null=True)),
                ('wppp_status_date', models.DateField(blank=True, null=True)),
                ('cooperator_agreement_number', models.CharField(blank=True, max_length=34, null=True)),
                ('gid', models.CharField(blank=True, max_length=16, null=True)),
                ('admin_open', models.CharField(blank=True, max_length=1, null=True)),
                ('last_update', models.DateField()),
            ],
            options={
                'db_table': 'ii_grants',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Grants',
        ),
    ]
