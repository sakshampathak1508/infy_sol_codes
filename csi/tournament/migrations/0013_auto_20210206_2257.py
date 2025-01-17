# Generated by Django 3.1.4 on 2021-02-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0012_auto_20210129_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='draw2_file',
            field=models.FileField(blank=True, upload_to='tournament/files'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='draw2_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tournament',
            name='draw2_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='results2_file',
            field=models.FileField(blank=True, upload_to='tournament/files'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='results2_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tournament',
            name='results2_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
