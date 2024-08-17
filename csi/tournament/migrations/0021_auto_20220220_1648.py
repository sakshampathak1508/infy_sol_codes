# Generated by Django 3.1.4 on 2022-02-20 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0020_auto_20210404_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='event_category',
            field=models.CharField(choices=[('IBSF', 'IBSF'), ('ACBS', 'ACBS'), ('National', 'NATIONAL'), ('Invitation', 'INVITATION'), ('OpenEntry', 'OPEN ENTRY'), ('Professional', 'PROFESSIONAL'), ('State', 'STATE'), ('Corporate', 'CORPORATE')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='sports_category',
            field=models.CharField(choices=[('Billiards', 'BILLIARDS'), ('Snooker', 'SNOOKER'), ('6REDS', '6REDS'), ('10REDS', '10REDS'), ('Pool', 'POOL'), ('Carrom', 'CARROM'), ('Cue-Sports', 'CUE SPORTS')], default='', max_length=50),
        ),
    ]