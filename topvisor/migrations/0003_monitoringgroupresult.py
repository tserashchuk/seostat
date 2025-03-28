# Generated by Django 5.1.6 on 2025-03-05 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topvisor', '0002_monitoringgroup_filterbygroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitoringGroupResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg', models.CharField(blank=True, max_length=200, verbose_name='Домен для мониторинга')),
                ('median', models.CharField(blank=True, max_length=200, verbose_name='ID проекта в топвизор')),
                ('visibility', models.CharField(blank=True, max_length=200, verbose_name='ID группы ключей')),
                ('top1_3', models.CharField(blank=True, max_length=200, verbose_name='В ТОП3')),
                ('top1_10', models.CharField(blank=True, max_length=200, verbose_name='В ТОП10')),
                ('top11_30', models.CharField(blank=True, max_length=200, verbose_name='В ТОП11-30')),
                ('top31_50', models.CharField(blank=True, max_length=200, verbose_name='В ТОП30-50')),
                ('top51_100', models.CharField(blank=True, max_length=200, verbose_name='В ТОП50-100')),
                ('top101_1000', models.CharField(blank=True, max_length=200, verbose_name='В ТОП101-1000')),
                ('date_from_topvisor_from', models.CharField(blank=True, max_length=200, verbose_name='Даты прилетевшие с топвизора c')),
                ('date_from_topvisor_to', models.CharField(blank=True, max_length=200, verbose_name='Даты прилетевшие с топвизора по')),
                ('date_sended_to_topvisor', models.CharField(blank=True, max_length=200, verbose_name='Дата отправленная и от нее -7 дней')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topvisor.monitoringgroup')),
            ],
        ),
    ]
