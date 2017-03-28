# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 23:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('g1', '0003_auto_20170327_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='dataEHoradeInicio',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='data e hora inicio'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='logotipo',
            field=models.TextField(blank=True, null=True, verbose_name='logotipo'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='palavrasChave',
            field=models.TextField(blank=True, null=True, verbose_name='palavras chaves'),
        ),
    ]