# Generated by Django 3.0.8 on 2020-08-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kosumi', '0023_veturat_fotoja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klientat',
            name='dataTerheqjes',
            field=models.DateField(blank=True, null=True),
        ),
    ]
