# Generated by Django 3.1.4 on 2021-01-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20210103_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='caption',
            new_name='breaks',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='image_at_back',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='player',
            name='club',
        ),
        migrations.RemoveField(
            model_name='player',
            name='image_at_front',
        ),
        migrations.AddField(
            model_name='coache',
            name='Facebook_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='coache',
            name='Instagram_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='coache',
            name='Twitter_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='highest_achievements',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='practice_at',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='referee',
            name='Facebook_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='referee',
            name='Instagram_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='referee',
            name='Twitter_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='Employed_with',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='player',
            name='awards',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='highest_break_billiards',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='highest_break_snooker',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(default='', max_length=120),
        ),
    ]
