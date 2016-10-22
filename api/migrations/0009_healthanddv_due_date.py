# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_healthanddv_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthanddv',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
