# Generated by Django 3.2.dev20200704211321 on 2020-07-24 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('tweet_id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('threads', models.TextField()),
                ('threads_body', models.TextField()),
                ('dot_length', models.TextField()),
            ],
        ),
    ]
