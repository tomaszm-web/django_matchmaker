# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlike',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_users', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
