# Generated by Django 3.2.7 on 2021-09-13 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kosumi', '0008_pagesat_administrata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kandidatet',
            name='kandatet',
            field=models.IntegerField(default=2021),
        ),
        migrations.AlterField(
            model_name='pagesat',
            name='viti',
            field=models.IntegerField(default=2021),
        ),
        migrations.AlterField(
            model_name='pagesateinstruktorve',
            name='viti',
            field=models.IntegerField(default=2021),
        ),
    ]
