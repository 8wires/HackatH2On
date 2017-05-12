# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('name', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=1000)),
                ('multiplier', models.PositiveSmallIntegerField(default=1)),
                ('goal', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('value', models.PositiveSmallIntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='DropUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('challenges', models.ManyToManyField(to='dropchain.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('value', models.PositiveSmallIntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('value', models.PositiveSmallIntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=1, choices=[('1', '1'), ('2', '2'), ('3', '3')])),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('name', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=100)),
                ('goal', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='priority',
            name='project',
            field=models.OneToOneField(to='dropchain.Project'),
        ),
        migrations.AddField(
            model_name='priority',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dropuser',
            name='priorities',
            field=models.ForeignKey(to='dropchain.Priority'),
        ),
        migrations.AddField(
            model_name='dropuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='challenge',
            name='days',
            field=models.ManyToManyField(to='dropchain.Day'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='hours',
            field=models.ManyToManyField(to='dropchain.Hour'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='months',
            field=models.ManyToManyField(to='dropchain.Month'),
        ),
        migrations.AlterUniqueTogether(
            name='priority',
            unique_together=set([('user', 'project'), ('value', 'user')]),
        ),
    ]
