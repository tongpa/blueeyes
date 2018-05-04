# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-04 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenditureType',
            fields=[
                ('id_expenditure_type', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('active', models.BooleanField(default=1, max_length=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]