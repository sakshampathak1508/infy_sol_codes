# Generated by Django 3.1.4 on 2021-01-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_auto_20210103_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='slug',
            field=models.SlugField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
