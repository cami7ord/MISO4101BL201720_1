# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_species'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=256)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='species',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Species'),
        ),
    ]
