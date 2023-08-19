# Generated by Django 4.2.4 on 2023-08-13 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0052_alter_loan_approval_approval'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan_approval',
            name='Comments',
            field=models.TextField(default=None, help_text='Reason of Rejection', max_length=2000),
        ),
        migrations.AlterField(
            model_name='loan_approval',
            name='Approval',
            field=models.CharField(choices=[('reject', 'Reject'), ('approve', 'Approve'), ('pending', 'Pending')], default='pending', max_length=200),
        ),
    ]
