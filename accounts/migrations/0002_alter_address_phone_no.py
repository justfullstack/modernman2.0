# Generated by Django 5.0.6 on 2024-07-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone_no',
            field=models.IntegerField(default='0712345678'),
        ),
    ]
