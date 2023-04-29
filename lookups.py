from inventory.models import Product
import datetime

Product.objects.filter(name__exact="Tea black")#точный
Product.objects.filter(name__contains="Tea")#содержит
Product.objects.filter(id__in=[1, 3, 5])#в
Product.objects.filter(id__gt=3)#больше чем
Product.objects.filter(id__lt=4)#меньше чем
Product.objects.filter(content__startswith="Green")#начинается с
Product.objects.filter(name__endswith="Black")#заканчивается с
Product.objects.filter(id__range=(1, 3))#между включительно
Product.objects.filter(time_create__date=datetime.date(2023, 4, 29))#по дате
