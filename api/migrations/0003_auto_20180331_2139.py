# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-31 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_recipe_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
