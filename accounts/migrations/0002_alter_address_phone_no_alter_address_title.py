# Generated by Django 5.0.6 on 2024-06-28 01:08

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
        migrations.AlterField(
            model_name='address',
            name='title',
            field=models.CharField(choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.')], default=('MR', 'Mr.'), max_length=3),
        ),
    ]
