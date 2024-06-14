from django.db import migrations

def capitalize(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    for product in Product.objects.all():
        product.name = product.name.capitalize()
        product.save()

class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_productimage_image_and_more'),
    ]

    operations = [
        migrations.RunPython(
                    capitalize,
                    migrations.RunPython.noop
                    ),
    ]
