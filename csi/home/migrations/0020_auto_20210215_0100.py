# Generated by Django 3.1.4 on 2021-02-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20210129_1822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='writing_about',
            options={'verbose_name': 'Writing About', 'verbose_name_plural': 'Writing Abouts'},
        ),
        migrations.AddField(
            model_name='ranking',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
