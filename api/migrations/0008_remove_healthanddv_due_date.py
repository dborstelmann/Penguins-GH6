# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20161022_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthanddv',
            name='due_date',
        ),
    ]
