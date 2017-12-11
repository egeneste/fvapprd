# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-11 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LecturaTempHume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.FloatField(blank=True, null=True)),
                ('humedad', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('modulo', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('modulo', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('s_temperatura', models.CharField(choices=[('ON', 'ON'), ('OFF', 'OFF'), ('OUT', 'OUT')], default='ON', max_length=5)),
                ('s_humedad', models.CharField(choices=[('ON', 'ON'), ('OFF', 'OFF'), ('OUT', 'OUT')], default='ON', max_length=5)),
                ('s_sonido', models.CharField(choices=[('ON', 'ON'), ('OFF', 'OFF'), ('OUT', 'OUT')], default='ON', max_length=5)),
                ('s_humo', models.CharField(choices=[('ON', 'ON'), ('OFF', 'OFF'), ('OUT', 'OUT')], default='ON', max_length=5)),
                ('latitud', models.FloatField(blank=True, null=True)),
                ('longitud', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModuloUbicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modulo', models.CharField(max_length=8)),
                ('last_latitud', models.FloatField(blank=True, null=True)),
                ('last_longitud', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
