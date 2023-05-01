from django.contrib import admin

from inventory.models import Brand, Category, Tag, Product, Stock

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Stock)

