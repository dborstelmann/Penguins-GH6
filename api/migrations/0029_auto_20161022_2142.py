# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20161022_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continuummembers',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='continuummembers',
            name='services_offered',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='continuummembers',
            name='website',
            field=models.CharField(max_length=255),
        ),
    ]
