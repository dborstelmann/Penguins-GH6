# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20161022_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='sub_type_provided',
            field=models.FloatField(null=True),
        ),
    ]
