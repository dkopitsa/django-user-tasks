# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-29 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_tasks', '0002_artifact_file_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertaskartifact',
            name='url',
            field=models.URLField(blank=True, max_length=512),
        ),
    ]
