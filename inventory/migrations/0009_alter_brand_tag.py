# Generated by Django 4.2 on 2023-04-24 08:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0008_alter_stock_product_brand"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="tag",
            field=models.ManyToManyField(related_name="brand_tags", to="inventory.tag"),
        ),
    ]
