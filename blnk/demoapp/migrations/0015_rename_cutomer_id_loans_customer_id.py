# Generated by Django 4.2.4 on 2023-08-10 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0014_loans_cutomer_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loans',
            old_name='cutomer_id',
            new_name='customer_id',
        ),
    ]