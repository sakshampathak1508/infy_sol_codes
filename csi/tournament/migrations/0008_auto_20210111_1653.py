# Generated by Django 3.1.4 on 2021-01-11 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0007_auto_20210111_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='tournament_image2',
            field=models.ImageField(blank=True, null=True, upload_to='tournament/images'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='tournament_image3',
            field=models.ImageField(blank=True, null=True, upload_to='tournament/images'),
        ),
    ]
