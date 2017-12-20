# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_auto_20171220_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='name',
            field=jsonfield.fields.JSONField(null=True, blank=True),
        ),
    ]
