# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-13 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FullForms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortForm', models.CharField(max_length=255)),
                ('fullForm', models.CharField(max_length=255)),
            ],
        ),
    ]
