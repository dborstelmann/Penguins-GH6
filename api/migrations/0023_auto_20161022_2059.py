# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20161022_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelters',
            name='name',
            field=models.CharField(max_length=63),
        ),
    ]
