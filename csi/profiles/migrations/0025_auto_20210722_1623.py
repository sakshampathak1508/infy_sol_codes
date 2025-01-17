# Generated by Django 3.1.4 on 2021-07-22 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0024_auto_20210722_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='entry_system',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='club',
            name='manager_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='club',
            name='timing_from',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='timing_to',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
