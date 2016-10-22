# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_client_war_participated'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='war_participated',
            field=django.contrib.postgres.fields.ArrayField(default=[], base_field=models.IntegerField(), size=None),
        ),
    ]
