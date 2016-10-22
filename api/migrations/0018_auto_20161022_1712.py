# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20161022_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='discharge_status',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='military_branch',
            field=models.IntegerField(null=True),
        ),
    ]
