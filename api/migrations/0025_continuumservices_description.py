# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20161022_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='continuumservices',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
