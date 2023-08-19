# Generated by Django 4.2.4 on 2023-08-13 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0065_alter_investment_approval_deposit_confirmation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment_approval',
            name='Deposit_Confirmation',
            field=models.CharField(choices=[('reject', 'Reject'), ('pending', 'Pending'), ('confirm', 'Approve')], default='pending', max_length=200),
        ),
        migrations.AlterField(
            model_name='loan_approval',
            name='Approval',
            field=models.CharField(choices=[('reject', 'Reject'), ('pending', 'Pending'), ('approve', 'Approve')], default='pending', max_length=200),
        ),
    ]
