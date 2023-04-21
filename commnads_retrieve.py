from inventory.models import Tag
from django.shortcuts import get_object_or_404
from django.db.models import Q

Tag.objects.get(id=1) #Получение только одного объекта
Tag.objects.get_or_create(name="django-react") #Получение одного объекта, при отсутсвии создание его
get_object_or_404(Tag, name="django-react") #Получение одного объекта, при отсутсвии ошибка 404

Tag.objects.all().filter(id=4) #Фильтр по айди
Tag.objects.filter(id=4)#Фильтр по айди
Tag.objects.exclude(id=3)#Фильтр исключить по айди

Tag.objects.filter(name="django") | Tag.objects.filter( name="react")#Фильтр используя ИЛИ
Tag.objects.filter(Q(id=2) | Q(id=5))#Фильтр используя ИЛИ
Tag.objects.filter(id__gt=2)#Фильтр по ГОТОВЫМ ПАРАМЕТРАМ (Больше чем)
Tag.objects.filter(name__startswith="d")#Фильтр по ГОТОВЫМ ПАРАМЕТРАМ (начинается с)