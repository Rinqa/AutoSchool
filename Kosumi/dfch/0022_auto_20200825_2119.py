# Generated by Django 3.0.8 on 2020-08-25 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kosumi', '0021_auto_20200825_2111'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vetyrat',
            new_name='Veturat',
        ),
        migrations.AddField(
            model_name='instruktori',
            name='vetura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Kosumi.Veturat'),
        ),
    ]
