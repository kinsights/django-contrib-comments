# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


is_abstract = lambda: getattr(settings, 'DJANGO_COMMENTS_ABSTRACT', False)


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0001_initial'),
    ]

    operations = []

    if not is_abstract():
        operations.append(
            migrations.AlterField(
                model_name='comment',
                name='user_email',
                field=models.EmailField(
                    max_length=254, verbose_name="user's email address",
                    blank=True),
            )
        )
