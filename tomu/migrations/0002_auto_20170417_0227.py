# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 02:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tomu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatter',
            options={'permissions': (('owner', 'Configurate bot'), ('mod', 'modify lists, edit-delete reminders, edit-delete items in list, temp-hide a user'), ('user', 'Create polls, reminders, add items to lists')), 'verbose_name': 'Chatter', 'verbose_name_plural': 'Chatters'},
        ),
    ]
