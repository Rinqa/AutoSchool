# Generated by Django 3.0.8 on 2020-08-25 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kosumi', '0022_auto_20200825_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='veturat',
            name='fotoja',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
