# Generated by Django 3.1.4 on 2021-07-22 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_auto_20210722_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]