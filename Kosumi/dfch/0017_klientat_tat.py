# Generated by Django 3.0.8 on 2020-08-24 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kosumi', '0016_tat'),
    ]

    operations = [
        migrations.AddField(
            model_name='klientat',
            name='tat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Kosumi.tat'),
        ),
    ]