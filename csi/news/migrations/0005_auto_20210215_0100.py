# Generated by Django 3.1.4 on 2021-02-14 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_newse_news_desc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newse',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]