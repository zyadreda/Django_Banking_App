# Generated by Django 4.2.4 on 2023-08-12 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0026_rename_loan_requests_loan_request'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Loan_Request',
            new_name='Loan_req',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='loan_term',
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_type',
            field=models.CharField(choices=[('short', 'Short'), ('intermediate', 'Intermediate'), ('long', 'Long')], default='short', max_length=100),
        ),
    ]
