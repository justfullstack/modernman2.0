# Generated by Django 5.0.6 on 2024-06-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_category_slug_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_count',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='product-thumbnails'),
        ),
    ]
