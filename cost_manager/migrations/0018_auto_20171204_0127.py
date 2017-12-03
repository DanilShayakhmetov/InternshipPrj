# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cost_manager', '0017_auto_20171203_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_transaction',
            name='account_jornal_status',
            field=models.CharField(choices=[('+', 'Приход'), ('-', 'Расход')], default='Приход', max_length=10, verbose_name='Operation status:'),
        ),
        migrations.AlterField(
            model_name='account_transaction',
            name='account_transaction_amount',
            field=models.IntegerField(default=0, verbose_name='Amount:'),
        ),
        migrations.AlterField(
            model_name='account_transaction',
            name='account_transaction_comment',
            field=models.CharField(default='comment...', max_length=30, verbose_name='comment:'),
        ),
        migrations.AlterField(
            model_name='account_transaction',
            name='account_transaction_currency',
            field=models.CharField(blank=True, choices=[('USD', 'dollars'), ('EUR', 'euro'), ('RUR', 'rubles')], default='rubles', max_length=10, verbose_name='Currency:'),
        ),
        migrations.AlterField(
            model_name='account_transaction',
            name='account_transaction_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date/time:'),
        ),
        migrations.AlterField(
            model_name='account_transaction',
            name='account_transaction_expenditure_name',
            field=models.CharField(help_text='Введите статью расходов или источник дохода', max_length=30, verbose_name='Expenditure name:'),
        ),
        migrations.AlterField(
            model_name='account_transaction',
            name='bank_account_title',
            field=models.CharField(blank=True, help_text='Введите имя счета, например: Основной \n Валютный \n Сберегательный', max_length=30, verbose_name='Account Name:'),
        ),
    ]