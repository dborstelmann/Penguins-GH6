# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20161022_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continuummembers',
            name='services_offered',
            field=models.CharField(max_length=31, null=True),
        ),
    ]
