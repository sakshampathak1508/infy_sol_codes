# Generated by Django 3.1.4 on 2021-04-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0018_tournament_collecting_fee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration_fee',
            options={'verbose_name': 'Registration Fees', 'verbose_name_plural': 'Registration Fees'},
        ),
        migrations.AddField(
            model_name='tournament',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
