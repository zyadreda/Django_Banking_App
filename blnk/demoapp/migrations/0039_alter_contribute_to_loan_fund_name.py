# Generated by Django 4.2.4 on 2023-08-13 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0038_alter_contribute_to_loan_fund_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribute_to_loan_fund',
            name='name',
            field=models.CharField(choices=[], max_length=200),
        ),
    ]
