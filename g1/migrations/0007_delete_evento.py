# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 23:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('g1', '0006_delete_pessoa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Evento',
        ),
    ]
