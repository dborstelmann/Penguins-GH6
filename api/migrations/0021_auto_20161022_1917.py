# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20161022_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=63, null=True)),
                ('last_name', models.CharField(max_length=63, null=True)),
                ('why', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=63, null=True)),
                ('address', models.CharField(max_length=63, null=True)),
                ('birthday', models.DateField()),
                ('ethnicity', models.IntegerField(default=99)),
                ('gender', models.IntegerField(default=99)),
                ('veteran', models.IntegerField(default=99)),
                ('family', models.CharField(max_length=63, null=True)),
                ('domestic_violence', models.IntegerField(null=True)),
                ('pregnancy', models.BooleanField()),
                ('drug', models.BooleanField()),
                ('urgency', models.FloatField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='test',
            name='user',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
