# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-29 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poemese', '0015_remove_relacoesamizade_status_aprovacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='avaliacao',
            field=models.IntegerField(choices=[('1', 'Péssimo'), ('2', 'Ruim'), ('3', 'Mediano'), ('4', 'Bom'), ('5', 'Excelente')], default=1),
        ),
    ]
