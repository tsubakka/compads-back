# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_client_bank_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='birthdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
