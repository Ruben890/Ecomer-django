# Generated by Django 4.2.7 on 2023-11-23 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pimages',
            new_name='images',
        ),
    ]
