# Generated by Django 4.0.5 on 2022-10-24 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_seller_name_product_seller_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='seller_id',
            new_name='seller_name',
        ),
    ]
