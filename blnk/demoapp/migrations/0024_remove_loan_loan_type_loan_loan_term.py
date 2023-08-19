# Generated by Django 4.2.4 on 2023-08-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0023_person_time_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='loan_type',
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_term',
            field=models.CharField(choices=[('3 months', '3 months'), ('intermediate', 'Intermediate'), ('long', 'Long')], default='3 months', max_length=100),
        ),
    ]
