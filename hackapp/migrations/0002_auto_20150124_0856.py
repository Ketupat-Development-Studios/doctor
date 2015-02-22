# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='essay',
            name='title',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='essay',
            name='url',
            field=models.TextField(default='u71z3d'),
            preserve_default=False,
        ),
    ]
