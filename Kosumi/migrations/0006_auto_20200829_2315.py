# Generated by Django 3.0.8 on 2020-08-29 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kosumi', '0005_auto_20200829_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='klientat',
            old_name='kandatet',
            new_name='kandidatet',
        ),
    ]
