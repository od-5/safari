# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_groupscomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='description',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
    ]
