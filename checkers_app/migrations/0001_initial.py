# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-11 03:08
from __future__ import unicode_literals

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
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_session', models.BooleanField(default=False)),
                ('which_player', models.PositiveSmallIntegerField(default=0)),
                ('jumped', models.BooleanField(default=False)),
                ('turn_over', models.BooleanField(default=False)),
                ('black_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='black_player', to=settings.AUTH_USER_MODEL)),
                ('red_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('king_Status', models.BooleanField(default=False)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_coordinate', models.PositiveSmallIntegerField(default=0)),
                ('y_coordinate', models.PositiveSmallIntegerField(default=0)),
                ('piece_id', models.BooleanField(default=False)),
                ('black_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkers_app.Piece')),
            ],
        ),
    ]
