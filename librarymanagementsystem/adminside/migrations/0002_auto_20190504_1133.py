# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-04 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
