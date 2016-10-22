# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20161022_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomebenefits',
            name='earned_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='incomebenefits',
            name='income_from_any_source',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='incomebenefits',
            name='ssdi_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='incomebenefits',
            name='ssi_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='incomebenefits',
            name='total_monthly_income',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='incomebenefits',
            name='unemployment_amount',
            field=models.FloatField(null=True),
        ),
    ]
