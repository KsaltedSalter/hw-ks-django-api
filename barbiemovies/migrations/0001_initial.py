# Generated by Django 3.2.8 on 2021-10-23 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BarbieMovies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('year', models.CharField(max_length=10)),
                ('barbies_char', models.CharField(max_length=70)),
                ('animal_friend', models.CharField(max_length=70)),
            ],
        ),
    ]
