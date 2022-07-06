# Generated by Django 4.0.5 on 2022-07-03 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product_phot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='phot',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]