# Generated by Django 3.1.4 on 2021-01-03 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20210103_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='coache',
            name='award',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='referee',
            name='award',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
