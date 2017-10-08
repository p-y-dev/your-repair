# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Название видео')),
                ('iframe', models.CharField(help_text="Чтобы вставить iframe, нужно на youtube под видео нажать на 'поделиться', затем нажать на встроить, и скопировать iframe. Пример iframe: <iframe width='560' height='315' src='https://www.youtube.com/embed/xAACRitp4eA' frameborder='0' allowfullscreen></iframe>'", max_length=9000, verbose_name='iframe видео')),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Видео',
                'ordering': ('-my_order',),
                'verbose_name': 'Видео',
            },
        ),
    ]
