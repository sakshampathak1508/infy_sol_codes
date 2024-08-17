# Generated by Django 3.1.4 on 2021-02-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0013_auto_20210206_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='draw3_file',
            field=models.FileField(blank=True, upload_to='tournament/files'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='draw3_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tournament',
            name='draw3_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='draw4_file',
            field=models.FileField(blank=True, upload_to='tournament/files'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='draw4_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tournament',
            name='draw4_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='draw5_file',
            field=models.FileField(blank=True, upload_to='tournament/files'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='draw5_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tournament',
            name='draw5_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='results3_file',
            field=models.FileField(blank=True, upload_to='tournament/files'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='results3_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tournament',
            name='results3_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='results4_file',
            field=models.FileField(blank=True, upload_to='tournament/files'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='results4_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tournament',
            name='results4_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='results5_file',
            field=models.FileField(blank=True, upload_to='tournament/files'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='results5_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tournament',
            name='results5_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
