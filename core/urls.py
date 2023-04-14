from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create/", views.create),
]
