# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-18 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='板块名称')),
                ('desc', models.CharField(max_length=100, verbose_name='板块描述')),
                ('manager', models.CharField(max_length=30, verbose_name='管理员名称')),
            ],
        ),
    ]
