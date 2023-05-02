from django.shortcuts import render

from django.http import HttpResponse

from inventory.models import Brand




def create(request):

    # items = Brand.objects.select_related('category')
    items = Brand.objects.prefetch_related('tag')
    
    #
    for item in items:
        for i in item.tag.all():
            i

    return render(request)