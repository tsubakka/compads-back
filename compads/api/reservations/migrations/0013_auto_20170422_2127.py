# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 21:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0012_auto_20170422_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajanlat',
            name='ajanlatado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ajanlatado_text', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ajanlat',
            name='ugyfel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ugyfel_text', to='clients.Client'),
        ),
    ]
