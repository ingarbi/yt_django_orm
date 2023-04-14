from django.shortcuts import render

from django.http import HttpResponse

from inventory.models import Brand

def create(request):

    Brand.objects.create(brand_id=5, name="requested Brand")

    return HttpResponse("Added")