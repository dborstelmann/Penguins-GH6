# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20161022_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='client',
            name='veteran',
            field=models.BooleanField(),
        ),
    ]
