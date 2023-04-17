from django.contrib import admin

from inventory.models import Brand, Category, Tag

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Tag)

