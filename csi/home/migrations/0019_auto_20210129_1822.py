# Generated by Django 3.1.4 on 2021-01-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20210126_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranking',
            name='category',
            field=models.CharField(choices=[('Men-Ranking-Billiards', 'Men-Ranking-Billiards'), ('Men-Ranking-Snooker', 'Men-Ranking-Snooker'), ('Women-Ranking-Billiards', 'Women-Ranking-Billiards'), ('Women-Ranking-Snooker', 'Women-Ranking-Snooker')], default='', max_length=100),
        ),
    ]
