# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-30 14:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poemese', '0017_auto_20171130_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='titulo',
            new_name='titulo_book',
        ),
    ]
