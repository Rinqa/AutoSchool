# Generated by Django 3.0.8 on 2020-08-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kosumi', '0029_auto_20200827_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veturat',
            name='fotoja',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
