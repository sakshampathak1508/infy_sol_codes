# Generated by Django 3.1.4 on 2021-01-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newse',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newse',
            name='news_title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
