# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Blog_post/Files/%Y/%m'),
        ),
    ]
