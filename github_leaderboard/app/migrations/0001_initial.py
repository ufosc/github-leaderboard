# Generated by Django 3.1.7 on 2021-03-15 12:47

import app.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=github_leaderboard.app.models.Result.default_score)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start', models.DateTimeField(default=github_leaderboard.app.models.Leaderboard.default_start_datetime)),
                ('end', models.DateTimeField(default=github_leaderboard.app.models.Leaderboard.default_end_datetime)),
                ('repo_url', models.URLField(blank=True, null=True)),
                ('access_token', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                            to=settings.AUTH_USER_MODEL)),
                ('results', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                              to='app.result')),
            ],
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodeid', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('url', models.URLField()),
                ('html_url', models.URLField()),
                ('timestamp', models.DateTimeField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('leaderboard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                  to='app.leaderboard')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                           to=settings.AUTH_USER_MODEL)),
           ],
        ),
    ]
