# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-25 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poemese', '0012_auto_20171125_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='capa_livro',
            field=models.ImageField(blank=True, null=True, upload_to='media/book-cover/'),
        ),
    ]
