# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_auto_20161023_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='uuid',
            field=models.CharField(max_length=63, null=True),
        ),
    ]
