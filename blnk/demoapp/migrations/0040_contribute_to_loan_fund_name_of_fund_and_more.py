# Generated by Django 4.2.4 on 2023-08-13 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0039_alter_contribute_to_loan_fund_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribute_to_loan_fund',
            name='Name_of_Fund',
            field=models.CharField(choices=[('Check Loan Funds First', 'Check Loan Funds First')], default=None, help_text='Check Loan Funds for the available investments', max_length=200),
        ),
        migrations.AddField(
            model_name='contribute_to_loan_fund',
            name='amount',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='contribute_to_loan_fund',
            name='date_of_deposit',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contribute_to_loan_fund',
            name='name',
            field=models.CharField(help_text='Enter Your Name', max_length=200),
        ),
    ]
