# Generated by Django 4.0.4 on 2022-04-13 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='inventory_quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
