# Generated by Django 5.0.6 on 2024-06-14 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_productname_capitalize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=48, null=True, unique=True),
        ),
    ]
