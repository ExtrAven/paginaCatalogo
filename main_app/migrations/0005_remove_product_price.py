# Generated by Django 5.1rc1 on 2024-09-02 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
