# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20161022_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incomebenefits',
            old_name='other_incount_source_amount',
            new_name='other_income_source_amount',
        ),
    ]
