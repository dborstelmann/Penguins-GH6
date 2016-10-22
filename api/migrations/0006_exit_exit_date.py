# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_client_war_participated'),
    ]

    operations = [
        migrations.AddField(
            model_name='exit',
            name='exit_date',
            field=models.DateField(default=datetime.datetime(2016, 10, 22, 15, 54, 39, 651796)),
            preserve_default=False,
        ),
    ]
