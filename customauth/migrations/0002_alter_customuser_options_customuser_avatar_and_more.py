# Generated by Django 5.0.6 on 2024-06-17 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='media/avatars/default-avatar.png', null=True, upload_to='media/avatars/'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_employee',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_subscribed',
            field=models.BooleanField(blank=True, default=False, verbose_name='is_subscribed'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='date_joined'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=200, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.TextField(blank=True, max_length=30, null=True, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last_login'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.TextField(blank=True, max_length=30, null=True, verbose_name='last_name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.TextField(blank=True, max_length=150, null=True, verbose_name='password'),
        ),
    ]
