# Generated by Django 4.2.4 on 2023-08-11 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0017_alter_loans_customer_alter_loans_loan_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan_req',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_loan', models.CharField(max_length=100)),
                ('loan_amount', models.IntegerField()),
                ('time_log', models.TimeField(help_text='Enter the Exact time')),
            ],
        ),
    ]
