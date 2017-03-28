# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 00:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('g1', '0015_auto_20170327_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtigoAutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='artigocientifico',
            name='eventoCientifico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='g1.EventoCientifico'),
        ),
        migrations.AddField(
            model_name='artigoautor',
            name='ArtigoCientifico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='g1.ArtigoCientifico'),
        ),
        migrations.AddField(
            model_name='artigoautor',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='g1.Pessoa'),
        ),
    ]
