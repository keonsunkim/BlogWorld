# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=255,
                                            unique=True, verbose_name='email address')),
                ('representation_name', models.CharField(db_index=True,
                                                         max_length=30, unique=True, verbose_name='representation name')),
                ('date_of_birth', models.DateField(verbose_name='date of birth')),
                ('is_active', models.BooleanField(
                    default=True, verbose_name='is active')),
                ('is_admin', models.BooleanField(
                    default=False, verbose_name='is admin')),
                ('phone_number', models.IntegerField(verbose_name='phone number')),
                ('last_name', models.CharField(
                    max_length=30, verbose_name='family name')),
                ('first_name', models.CharField(
                    max_length=30, verbose_name='first name')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
