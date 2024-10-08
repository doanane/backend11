# Generated by Django 5.0.6 on 2024-07-17 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='details',
            field=models.CharField(default='No details provided', max_length=200),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='Unavailable', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='Unavailable', max_length=30),
        ),
    ]
