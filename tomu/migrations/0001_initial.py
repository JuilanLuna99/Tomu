# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chatter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Chatter',
                'verbose_name_plural': 'Chatters',
                'permissions': (('owner', 'Can do everything that a teacher can and configurate the bot'), ('teacher', 'Can modify the lists, '), ('mod', 'modify lists, edit-delete reminders, edit-delete items in list, temphide a user'), ('user', 'Create polls, reminders, add items in lists')),
            },
        ),
    ]
