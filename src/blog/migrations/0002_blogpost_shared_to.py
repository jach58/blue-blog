# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='shared_to',
            field=models.ManyToManyField(related_name='shared_posts', to='blog.Blog'),
        ),
    ]
