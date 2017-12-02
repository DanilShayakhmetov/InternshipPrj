# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost_manager', '0003_auto_20171202_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_journal',
            name='account_jornal_status',
            field=models.CharField(default=(('+', 'Приход'), ('-', 'Расход')), max_length=10),
        ),
        migrations.AddField(
            model_name='account_transaction',
            name='account_transaction_currency',
            field=models.CharField(default=(('USD', 'dollars'), ('EUR', 'euro'), ('RUR', 'rubles')), max_length=10),
        ),
    ]