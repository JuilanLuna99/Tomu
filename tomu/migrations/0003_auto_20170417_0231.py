# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 02:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tomu', '0002_auto_20170417_0227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatter',
            options={'verbose_name': 'Chatter', 'verbose_name_plural': 'Chatters'},
        ),
    ]
