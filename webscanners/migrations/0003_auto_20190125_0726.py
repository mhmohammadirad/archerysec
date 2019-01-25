# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-25 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscanners', '0002_auto_20181031_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='acunetix_scan_result_db',
            name='scanner',
            field=models.CharField(default='Acunetix', editable=False, max_length=15),
        ),
        migrations.AddField(
            model_name='arachni_scan_result_db',
            name='scanner',
            field=models.CharField(default='Arachni', editable=False, max_length=15),
        ),
        migrations.AddField(
            model_name='burp_scan_result_db',
            name='scanner',
            field=models.CharField(default='Burp Scanner', editable=False, max_length=15),
        ),
        migrations.AddField(
            model_name='netsparker_scan_result_db',
            name='scanner',
            field=models.CharField(default='Netsparker', editable=False, max_length=15),
        ),
        migrations.AddField(
            model_name='webinspect_scan_result_db',
            name='scanner',
            field=models.CharField(default='Webinspect', editable=False, max_length=15),
        ),
        migrations.AddField(
            model_name='zap_scan_results_db',
            name='scanner',
            field=models.CharField(default='ZAP Scanner', editable=False, max_length=15),
        ),
    ]
