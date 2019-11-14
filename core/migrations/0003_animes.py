# Generated by Django 2.2.7 on 2019-11-14 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191109_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animes',
            fields=[
                ('Aname', models.CharField(max_length=100, verbose_name='Nome_do_anime')),
                ('ID', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Anime',
                'verbose_name_plural': 'Animes',
                'ordering': ['Aname'],
            },
        ),
    ]