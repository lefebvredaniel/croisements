# Generated by Django 2.1.3 on 2018-11-22 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relations_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='r_artiste_documents',
            name='comment_relations',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]