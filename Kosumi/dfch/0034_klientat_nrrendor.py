# Generated by Django 3.0.8 on 2020-08-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kosumi', '0033_remove_klientat_kandidatet'),
    ]

    operations = [
        migrations.AddField(
            model_name='klientat',
            name='nrRendor',
            field=models.IntegerField(default=1),
        ),
    ]
