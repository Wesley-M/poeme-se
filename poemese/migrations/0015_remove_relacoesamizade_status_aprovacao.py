# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-26 13:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poemese', '0014_usuario_number_of_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relacoesamizade',
            name='status_aprovacao',
        ),
    ]