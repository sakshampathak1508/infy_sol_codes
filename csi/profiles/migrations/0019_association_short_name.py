# Generated by Django 3.1.4 on 2021-03-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_association_mobile_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='association',
            name='short_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
