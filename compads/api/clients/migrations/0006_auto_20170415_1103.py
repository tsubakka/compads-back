# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20170415_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_addresses', to='clients.Client'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_phones', to='clients.Client'),
        ),
    ]
