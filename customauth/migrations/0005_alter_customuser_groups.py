# Generated by Django 5.0.6 on 2024-06-25 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('customauth', '0004_alter_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.group'),
        ),
    ]
