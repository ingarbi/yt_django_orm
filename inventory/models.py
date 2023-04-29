from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Time_created")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Time_updated")
    is_published = models.BooleanField(default=True, verbose_name="Is_published")

    def __str__(self):
        return self.name

class Brand(models.Model):
    brand_id = models.PositiveBigIntegerField(primary_key=True, db_column="brand_id")
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="brands"
    )
    tag = models.ManyToManyField("Tag", related_name="brand_tags")

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
 