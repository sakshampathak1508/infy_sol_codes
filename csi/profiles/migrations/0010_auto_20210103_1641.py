# Generated by Django 3.1.4 on 2021-01-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20210103_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='coache',
            name='slug',
            field=models.SlugField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='slug',
            field=models.SlugField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='referee',
            name='slug',
            field=models.SlugField(default='', max_length=120),
            preserve_default=False,
        ),
    ]