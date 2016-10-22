# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_healthanddv_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomebenefits',
            name='alimony_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='incomebenefits',
            name='child_support_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='incomebenefits',
            name='ga_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='incomebenefits',
            name='pension_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='incomebenefits',
            name='tanf_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='incomebenefits',
            name='va_disability_service_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='incomebenefits',
            name='workers_comp_amount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='fa_amount',
            field=models.FloatField(null=True),
        ),
    ]
