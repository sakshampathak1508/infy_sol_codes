# Generated by Django 3.1.4 on 2021-01-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_tournament_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='show_on_concluded',
            field=models.BooleanField(default=False),
        ),
    ]
