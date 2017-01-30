# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0020_auto_20170126_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateselection',
            name='contest',
            field=models.ForeignKey(help_text='References the ``CandidateContest`` in which the selection is an option.', on_delete=django.db.models.deletion.CASCADE, related_name='candidate_selections', to='calaccess_processed.CandidateContest'),
        ),
    ]
