# Generated by Django 3.0.8 on 2020-08-21 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kosumi', '0007_auto_20200821_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klientat',
            name='nrRendor',
            field=models.IntegerField(),
        ),
    ]
