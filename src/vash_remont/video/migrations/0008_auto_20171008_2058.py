# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_auto_20171008_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='iframe',
        ),
        migrations.AddField(
            model_name='video',
            name='link_video',
            field=models.TextField(default='dawd', max_length=9000, verbose_name='Ссылка на видео'),
            preserve_default=False,
        ),
    ]
