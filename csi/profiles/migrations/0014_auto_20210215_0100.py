# Generated by Django 3.1.4 on 2021-02-14 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_remove_referee_award'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='referee',
            options={'verbose_name': 'Referee', 'verbose_name_plural': "Referee's"},
        ),
    ]