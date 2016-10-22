# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20161022_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phone',
            field=models.CharField(max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='why',
            field=models.CharField(max_length=1025, null=True),
        ),
    ]
