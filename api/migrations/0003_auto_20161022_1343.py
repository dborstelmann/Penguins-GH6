# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_client_continuummembers_continuumservices_disabilities_employmenteducation_enrollment_exit_healthand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='created',
        ),
        migrations.RemoveField(
            model_name='client',
            name='updated',
        ),
        migrations.AddField(
            model_name='client',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 22, 13, 43, 48, 507514)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 22, 13, 43, 57, 20051)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='disabilities',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='disabilities',
            name='date_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='employmenteducation',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='employmenteducation',
            name='date_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='date_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='exit',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='exit',
            name='date_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='healthanddv',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='healthanddv',
            name='date_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='incomebenefits',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='incomebenefits',
            name='date_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='date_updated',
            field=models.DateTimeField(),
        ),
    ]
