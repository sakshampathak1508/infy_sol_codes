# Generated by Django 3.1.4 on 2020-12-31 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210101_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='champ_sport1',
            field=models.CharField(blank=True, choices=[('Billiards', 'BILLIARDS'), ('Snooker', 'SNOOKER'), ('6REDS', '6REDS'), ('10REDS', '10REDS'), ('Pool', 'POOL'), ('Carrom', 'CARROM')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='champ_sport2',
            field=models.CharField(blank=True, choices=[('Billiards', 'BILLIARDS'), ('Snooker', 'SNOOKER'), ('6REDS', '6REDS'), ('10REDS', '10REDS'), ('Pool', 'POOL'), ('Carrom', 'CARROM')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='champ_sport3',
            field=models.CharField(blank=True, choices=[('Billiards', 'BILLIARDS'), ('Snooker', 'SNOOKER'), ('6REDS', '6REDS'), ('10REDS', '10REDS'), ('Pool', 'POOL'), ('Carrom', 'CARROM')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='champ_sport4',
            field=models.CharField(blank=True, choices=[('Billiards', 'BILLIARDS'), ('Snooker', 'SNOOKER'), ('6REDS', '6REDS'), ('10REDS', '10REDS'), ('Pool', 'POOL'), ('Carrom', 'CARROM')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='champ_sport5',
            field=models.CharField(blank=True, choices=[('Billiards', 'BILLIARDS'), ('Snooker', 'SNOOKER'), ('6REDS', '6REDS'), ('10REDS', '10REDS'), ('Pool', 'POOL'), ('Carrom', 'CARROM')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='champ_sport6',
            field=models.CharField(blank=True, choices=[('Billiards', 'BILLIARDS'), ('Snooker', 'SNOOKER'), ('6REDS', '6REDS'), ('10REDS', '10REDS'), ('Pool', 'POOL'), ('Carrom', 'CARROM')], default='', max_length=50),
        ),
    ]
