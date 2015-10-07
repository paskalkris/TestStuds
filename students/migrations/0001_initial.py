# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('dbirthday', models.DateField()),
                ('nstud', models.CharField(max_length=15)),
                ('cgroup', models.ForeignKey(to='groups.Group')),
            ],
        ),
    ]
