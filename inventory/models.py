from django.db import models


class Brand(models.Model):
    brand_id = models.PositiveBigIntegerField(primary_key=True, db_column="brand_id")
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
