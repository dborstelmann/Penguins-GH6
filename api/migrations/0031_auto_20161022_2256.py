# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20161022_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='associate_id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_updated',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='ethnicity',
            field=models.IntegerField(default=99, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.IntegerField(default=99, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='veteran',
            field=models.IntegerField(default=99, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='war_participated',
            field=django.contrib.postgres.fields.ArrayField(default=[], null=True, base_field=models.IntegerField(), size=None),
        ),
    ]
