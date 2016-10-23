# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20161022_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='continuummembers',
            name='criteria_required',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
