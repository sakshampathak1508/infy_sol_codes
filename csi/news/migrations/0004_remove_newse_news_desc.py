# Generated by Django 3.1.4 on 2021-01-06 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newse_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newse',
            name='news_desc',
        ),
    ]