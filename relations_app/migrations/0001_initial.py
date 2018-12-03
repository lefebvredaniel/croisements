# Generated by Django 2.1.3 on 2018-11-22 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artiste_nom', models.CharField(max_length=70)),
                ('artiste_prénom', models.CharField(max_length=70)),
                ('artiste_datenaissance', models.DateField(max_length=50)),
                ('artiste_datedeces', models.DateField(max_length=50)),
                ('artiste_wiki', models.URLField(blank=True)),
                ('artiste_biolight', models.CharField(blank=True, max_length=500)),
                ('artiste_nomjpg', models.CharField(default=models.CharField(max_length=70), max_length=500)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaires',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents_adresse', models.URLField()),
                ('documents_commentaires', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='R_artiste_documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artiste_nom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relations_app.Artiste')),
                ('documents_adresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relations_app.Documents')),
            ],
        ),
        migrations.AddField(
            model_name='commentaires',
            name='titre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='relations_app.Documents'),
        ),
    ]
