# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 07:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_auto_20170828_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_id', to='menus.PageModel'),
        ),
    ]
