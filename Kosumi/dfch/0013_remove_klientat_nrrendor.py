# Generated by Django 3.0.8 on 2020-08-22 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kosumi', '0012_klientat_vijimi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='klientat',
            name='nrRendor',
        ),
    ]
