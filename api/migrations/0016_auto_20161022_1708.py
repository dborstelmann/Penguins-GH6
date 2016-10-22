# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20161022_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='gender',
            field=models.IntegerField(default=99),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='veteran',
            field=models.IntegerField(default=99),
            preserve_default=False,
        ),
    ]
