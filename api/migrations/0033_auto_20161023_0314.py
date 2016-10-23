# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_continuummembers_criteria_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employmenteducation',
            name='date_created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='employmenteducation',
            name='date_updated',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='employmenteducation',
            name='employment_education_id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='employmenteducation',
            name='project_entry_id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='healthanddv',
            name='health_and_dv_id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='healthanddv',
            name='project_entry_id',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
