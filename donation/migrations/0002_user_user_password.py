# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_password',
            field=models.CharField(default='def_pass', max_length=100),
            preserve_default=False,
        ),
    ]
