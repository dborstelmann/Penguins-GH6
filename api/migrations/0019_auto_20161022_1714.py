# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20161022_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 22, 17, 14, 20, 176676)),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 22, 17, 14, 20, 176712)),
        ),
        migrations.AlterField(
            model_name='client',
            name='ethnicity',
            field=models.IntegerField(default=99),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=63, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.IntegerField(default=99),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=63, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='middle_name',
            field=models.CharField(max_length=63, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='social_security',
            field=models.CharField(max_length=63, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='veteran',
            field=models.IntegerField(default=99),
        ),
    ]
