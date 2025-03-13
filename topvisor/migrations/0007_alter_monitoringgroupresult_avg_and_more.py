# Generated by Django 5.1.6 on 2025-03-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topvisor', '0006_alter_monitoringgroup_name_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoringgroupresult',
            name='avg',
            field=models.CharField(blank=True, max_length=200, verbose_name='Средняя позиция'),
        ),
        migrations.AlterField(
            model_name='monitoringgroupresult',
            name='median',
            field=models.CharField(blank=True, max_length=200, verbose_name='Медиана'),
        ),
        migrations.AlterField(
            model_name='monitoringgroupresult',
            name='visibility',
            field=models.CharField(blank=True, max_length=200, verbose_name='Видимость'),
        ),
    ]
