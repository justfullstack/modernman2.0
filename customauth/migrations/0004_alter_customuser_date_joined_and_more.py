# Generated by Django 5.0.6 on 2024-06-24 18:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0003_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_joined'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='last_name'),
        ),
    ]
