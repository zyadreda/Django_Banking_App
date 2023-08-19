# Generated by Django 4.2.4 on 2023-08-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0068_alter_investment_approval_deposit_confirmation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Loan_req',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.AlterField(
            model_name='investment_approval',
            name='Comments',
            field=models.TextField(blank=True, default='', help_text='If Rejected, Write reason of Rejection', max_length=2000),
        ),
        migrations.AlterField(
            model_name='loan_approval',
            name='Approval',
            field=models.CharField(choices=[('pending', 'Pending'), ('reject', 'Reject'), ('approve', 'Approve')], default='pending', max_length=200),
        ),
        migrations.DeleteModel(
            name='Loan',
        ),
    ]