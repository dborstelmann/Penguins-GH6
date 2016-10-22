# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20161022_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='continuumservices',
            name='description',
        ),
        migrations.AlterField(
            model_name='continuumservices',
            name='name',
            field=models.CharField(max_length=63),
        ),
    ]
