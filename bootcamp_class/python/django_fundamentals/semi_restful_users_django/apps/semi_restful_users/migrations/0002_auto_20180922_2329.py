# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-22 23:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='last_name',
        ),
    ]