# Generated by Django 3.0.8 on 2020-09-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kosumi', '0007_auto_20200901_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagesat',
            name='Administrata',
            field=models.IntegerField(default=0),
        ),
    ]
