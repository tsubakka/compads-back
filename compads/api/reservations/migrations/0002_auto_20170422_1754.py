# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 17:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ajanlat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ajanlatado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='agytipus',
            options={'verbose_name': 'Ágytípus', 'verbose_name_plural': 'Ágytípusok'},
        ),
        migrations.AlterModelOptions(
            name='alapar',
            options={'verbose_name': 'Alapár', 'verbose_name_plural': 'Alapárak'},
        ),
        migrations.AlterModelOptions(
            name='szallas',
            options={'verbose_name': 'Szállás', 'verbose_name_plural': 'Szállások'},
        ),
        migrations.AlterModelOptions(
            name='szallasjelleg',
            options={'verbose_name': 'Szállás jelleg', 'verbose_name_plural': 'Szállás jellegek'},
        ),
        migrations.AlterModelOptions(
            name='szallasresz',
            options={'verbose_name': 'Szállásrész', 'verbose_name_plural': 'Szállásrészek'},
        ),
        migrations.AlterModelOptions(
            name='szallasresztipus',
            options={'verbose_name': 'Szállásrész típus', 'verbose_name_plural': 'Szállásrész típusok'},
        ),
        migrations.AlterModelOptions(
            name='szallastipus',
            options={'verbose_name': 'Szállás típus', 'verbose_name_plural': 'Szállás típusok'},
        ),
        migrations.AlterField(
            model_name='szallasresz',
            name='szallas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='szallas_szallasreszek', to='reservations.Szallas'),
        ),
    ]
