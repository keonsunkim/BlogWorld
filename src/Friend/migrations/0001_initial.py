# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-06 06:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowRelationShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='follow created')),
                ('followee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'follow relationship',
                'verbose_name_plural': 'follow relationships',
            },
        ),
        migrations.AlterUniqueTogether(
            name='followrelationship',
            unique_together=set([('follower', 'followee')]),
        ),
    ]