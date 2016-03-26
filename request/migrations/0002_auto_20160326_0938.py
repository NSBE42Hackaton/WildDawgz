# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestparams',
            name='OS',
            field=models.CharField(max_length=20, choices=[(b'OSX', b'Apple OSX'), (b'Windows', b'Windows'), (b'Linux', b'Linux')]),
        ),
        migrations.AlterField(
            model_name='requestparams',
            name='device',
            field=models.CharField(blank=True, max_length=20, choices=[(b'Desktop', b'Desktop'), (b'Laptop', b'Laptop'), (b'Tablet', b'Tablet')]),
        ),
        migrations.AlterField(
            model_name='requestparams',
            name='ethnicity',
            field=models.CharField(blank=True, max_length=20, choices=[(b'Hispanic', b'Hispanic'), (b'White', b'White'), (b'Black', b'Black'), (b'Asian', b'Asian or Pacific Islander'), (b'Native', b'American Indian or Alaskan Native'), (b'NA', b'Choose not to answer')]),
        ),
        migrations.AlterField(
            model_name='requestparams',
            name='gender',
            field=models.CharField(blank=True, max_length=20, choices=[(b'MALE', b'MALE'), (b'FEMALE', b'FEMALE'), (b'NA', b'Choose not to answer')]),
        ),
        migrations.AlterField(
            model_name='requestparams',
            name='need',
            field=models.CharField(max_length=20, choices=[(b'School', b'School'), (b'Personal', b'Personal')]),
        ),
    ]
