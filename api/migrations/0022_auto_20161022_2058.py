# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20161022_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shelters',
            name='last_updated',
            field=models.DateTimeField(null=True),
        ),
    ]
