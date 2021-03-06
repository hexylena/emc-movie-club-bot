# Generated by Django 4.0.4 on 2022-05-25 14:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieSuggestion',
            fields=[
                ('imdb_id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('year', models.IntegerField()),
                ('rating', models.FloatField()),
                ('ratings', models.IntegerField()),
                ('runtime', models.IntegerField()),
                ('watched', models.BooleanField()),
                ('cage_factor', models.BooleanField()),
                ('rock_factor', models.BooleanField()),
                ('expressed_interest', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
