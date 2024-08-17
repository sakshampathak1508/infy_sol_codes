# Generated by Django 3.1.4 on 2021-07-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0020_remove_association_pin_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('slug', models.SlugField(max_length=150)),
                ('address', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('state', models.CharField(blank=True, default='', max_length=100)),
                ('mobile_number', models.CharField(blank=True, default='', max_length=100)),
                ('email1', models.CharField(blank=True, default='', max_length=100)),
                ('email2', models.CharField(blank=True, default='', max_length=100)),
                ('phone_number1', models.CharField(blank=True, default='', max_length=100)),
                ('phone_number2', models.CharField(blank=True, default='', max_length=100)),
                ('phone_number3', models.CharField(blank=True, default='', max_length=100)),
                ('snooker_tables', models.CharField(blank=True, default='', max_length=100)),
                ('pool_tables', models.CharField(blank=True, default='', max_length=100)),
                ('carrom_tables', models.CharField(blank=True, default='', max_length=100)),
                ('logo', models.ImageField(upload_to='profile/images')),
                ('image1', models.ImageField(upload_to='profile/images')),
                ('image2', models.ImageField(blank=True, upload_to='profile/images')),
                ('insta_url', models.URLField(blank=True)),
                ('facebook_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]