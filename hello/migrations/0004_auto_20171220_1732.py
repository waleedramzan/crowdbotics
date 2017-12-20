# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_animal_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('animal_type', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='type',
            field=models.ForeignKey(related_name='type_of_animal', default=123, to='hello.Types'),
            preserve_default=False,
        ),
    ]
