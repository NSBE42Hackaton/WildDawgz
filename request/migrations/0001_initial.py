# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestParams',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_Name', models.CharField(max_length=50)),
                ('first_Name', models.CharField(max_length=50)),
                ('last_Name', models.CharField(max_length=50)),
                ('OS', models.CharField(max_length=20, choices=[(b'MAC', b'Apple OSX'), (b'WIN', b'Windows'), (b'LIN', b'Linux')])),
                ('device', models.CharField(blank=True, max_length=20, choices=[(b'DES', b'Desktop'), (b'LAP', b'Laptop'), (b'TAB', b'Tablet')])),
                ('need', models.CharField(max_length=20, choices=[(b'SCH', b'School'), (b'PER', b'Personal')])),
                ('software', models.CharField(max_length=20, choices=[(b'PHO', b'Adobe Photoshop'), (b'ILL', b'Adobe Illustrator'), (b'SOL', b'SolidWorks'), (b'XCO', b'Xcode Development'), (b'AND', b'Android Development'), (b'HTM', b'HTML'), (b'JAV', b'Java'), (b'PYT', b'Python'), (b'CPL', b'C++'), (b'UNI', b'Unity')])),
                ('grade', models.CharField(blank=True, max_length=20, choices=[(b'FIR', b'1st - 4th'), (b'FIF', b'5th - 6th'), (b'SIX', b'6th - 8th'), (b'EIG', b'8th - 12th'), (b'COL', b'College'), (b'NIL', b'NONE')])),
                ('gender', models.CharField(blank=True, max_length=20, choices=[(b'MAL', b'MALE'), (b'FEM', b'FEMALE'), (b'NA', b'Choose not to answer')])),
                ('ethnicity', models.CharField(blank=True, max_length=20, choices=[(b'MAL', b'Hispanic'), (b'WHI', b'White'), (b'BLA', b'Black'), (b'ASI', b'Asian or Pacific Islander'), (b'AME', b'American Indian or Alaskan Native'), (b'NA', b'Choose not to answer')])),
                ('zip_Code', models.CharField(max_length=10)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'get_latest_by': 'updated',
            },
        ),
    ]
