# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tomu', '0007_auto_20170417_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatter',
            name='permissions',
        ),
        migrations.AddField(
            model_name='chatter',
            name='tempPassword',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='chatter',
            name='discord_username',
            field=models.CharField(max_length=32),
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
    ]
