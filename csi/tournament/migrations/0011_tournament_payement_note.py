# Generated by Django 3.1.4 on 2021-01-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0010_auto_20210125_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='payement_note',
            field=models.TextField(blank=True),
        ),
    ]
