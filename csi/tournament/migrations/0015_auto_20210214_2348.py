# Generated by Django 3.1.4 on 2021-02-14 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0014_auto_20210207_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournament',
            old_name='show_on_concluded',
            new_name='hide_from_concluded',
        ),
    ]
