# Generated by Django 3.1.4 on 2021-01-03 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210104_0113'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Support',
        ),
        migrations.AddField(
            model_name='writing_about',
            name='content_support_us',
            field=models.TextField(blank=True),
        ),
    ]
