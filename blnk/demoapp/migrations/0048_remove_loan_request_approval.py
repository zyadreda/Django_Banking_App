# Generated by Django 4.2.4 on 2023-08-13 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0047_rename_loan_options_loan_option_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan_request',
            name='approval',
        ),
    ]
