# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-06 03:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_organization', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_oef', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OutcomeArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OutputToSubOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('percent', models.DecimalField(decimal_places=2, default=1, help_text='Percentage of output on suboutcome area', max_digits=10)),
                ('output', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Output')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('otis_id', models.IntegerField(blank=True)),
                ('title', models.CharField(max_length=255)),
                ('goal', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Donor')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('level', models.IntegerField(choices=[(1, 'LEVEL 1'), (2, 'LEVEL 2'), (3, 'LEVEL 3'), (4, 'LEVEL 4'), (5, 'LEVEL 5'), (6, 'LEVEL 6'), (7, 'LEVEL 7'), (8, 'LEVEL 8'), (9, 'LEVEL 9'), (10, 'LEVEL 10'), (11, 'LEVEL 11'), (12, 'LEVEL 12'), (13, 'LEVEL 13'), (14, 'LEVEL 14'), (15, 'LEVEL 15'), (16, 'LEVEL 16'), (17, 'LEVEL 17'), (18, 'LEVEL 18'), (19, 'LEVEL 19'), (20, 'LEVEL 20'), (21, 'LEVEL 21'), (22, 'LEVEL 22'), (23, 'LEVEL 23'), (24, 'LEVEL 24'), (25, 'LEVEL 25'), (26, 'LEVEL 26'), (27, 'LEVEL 27'), (28, 'LEVEL 28'), (29, 'LEVEL 29'), (30, 'LEVEL 30'), (31, 'LEVEL 31'), (32, 'LEVEL 32')], default=1)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.OutcomeArea')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.SubOutcome')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SupportingDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='supporting_documents/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='suboutcome',
            name='supporting_documents',
            field=models.ManyToManyField(blank=True, to='projects.SupportingDocument'),
        ),
        migrations.AddField(
            model_name='outputtosuboutcome',
            name='suboutcome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.SubOutcome'),
        ),
        migrations.AddField(
            model_name='output',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AddField(
            model_name='output',
            name='suboutcome_areas',
            field=models.ManyToManyField(blank=True, through='projects.OutputToSubOutcome', to='projects.SubOutcome'),
        ),
        migrations.AddField(
            model_name='objective',
            name='outcome_areas',
            field=models.ManyToManyField(blank=True, to='projects.OutcomeArea'),
        ),
        migrations.AddField(
            model_name='objective',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='suboutcome_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.SubOutcome'),
        ),
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]