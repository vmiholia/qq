# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-08 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_auto_20180309_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_marks',
            name='gradebookitem',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
