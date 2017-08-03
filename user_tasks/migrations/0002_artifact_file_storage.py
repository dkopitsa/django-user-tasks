# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 16:12
from __future__ import unicode_literals

from django.db import migrations, models

from user_tasks.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user_tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertaskartifact',
            name='file',
            field=models.FileField(
                blank=True, null=True, storage=settings.USER_TASKS_ARTIFACT_STORAGE, upload_to='user_tasks/%Y/%m/%d/'),
        ),
    ]
