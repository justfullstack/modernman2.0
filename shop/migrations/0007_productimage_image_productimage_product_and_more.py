# Generated by Django 5.0.6 on 2024-06-14 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='product-images'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='thumbnail',
            field=models.ImageField(upload_to='product-thumbnails'),
        ),
    ]
