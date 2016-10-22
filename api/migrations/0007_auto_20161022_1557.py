# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_exit_exit_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exit',
            old_name='written_after_care_pan',
            new_name='written_after_care_plan',
        ),
    ]
