# Generated by Django 3.1.4 on 2021-01-03 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20210103_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referee',
            name='award',
        ),
    ]