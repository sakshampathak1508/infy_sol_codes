# Generated by Django 3.1.4 on 2021-01-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_champion'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='profile_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
