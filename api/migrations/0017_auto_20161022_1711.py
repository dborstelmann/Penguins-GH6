# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20161022_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='year_entered',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='year_exited',
            field=models.IntegerField(null=True),
        ),
    ]
