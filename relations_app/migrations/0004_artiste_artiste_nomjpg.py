# Generated by Django 2.0 on 2018-11-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relations_app', '0003_auto_20181120_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='artiste',
            name='artiste_nomjpg',
            field=models.CharField(default=models.CharField(max_length=70), max_length=500),
        ),
    ]