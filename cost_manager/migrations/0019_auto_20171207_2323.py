# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cost_manager', '0018_auto_20171204_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_account_title', models.CharField(blank=True, help_text='Введите имя счета, например: Основной \n Валютный \n Сберегательный', max_length=30, verbose_name='Account Name:')),
            ],
            options={
                'db_table': 'User Account',
            },
        ),
        migrations.AddField(
            model_name='account_transaction',
            name='bank_account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cost_manager.Bank_Account'),
            preserve_default=False,
        ),
    ]