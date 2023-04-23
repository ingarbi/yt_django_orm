from django.db import models


class Brand(models.Model):
    brand_id = models.PositiveBigIntegerField(primary_key=True, db_column="brand_id")
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="brands"
    )
    tag = models.ManyToManyField("Tag")

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    product_brand = models.OneToOneField(
        Brand, on_delete=models.PROTECT, related_name="stock_brand"
    )
    quantity = models.IntegerField(default=0)
