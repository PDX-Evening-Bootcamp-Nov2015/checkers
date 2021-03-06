# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-13 04:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkers_app', '0002_auto_20160213_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='game_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='checkers_app.Game'),
        ),
        migrations.AlterField(
            model_name='space',
            name='piece_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='checkers_app.Piece'),
        ),
    ]
