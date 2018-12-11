# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-06 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=35, unique=True, verbose_name='tag slug')),
                ('word', models.CharField(max_length=35, verbose_name='tag word')),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'filter tag',
                'verbose_name_plural': 'filter tags',
            },
        ),
        migrations.CreateModel(
            name='FilterTagRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('filter_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tag.FilterTag')),
                ('general_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.GeneralPost')),
            ],
            options={
                'verbose_name': 'filter tag relation',
                'verbose_name_plural': 'filter tag relations',
            },
        ),
    ]
