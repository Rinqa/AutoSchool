# Generated by Django 3.0.8 on 2020-08-21 09:08

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kosumi', '0005_auto_20200820_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='klientat',
            name='nrRendor',
            field=models.IntegerField(default=0),
        ),
    ]
