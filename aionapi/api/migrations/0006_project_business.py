# Generated by Django 5.0.7 on 2024-08-22 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_business_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='business',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.business'),
        ),
    ]
