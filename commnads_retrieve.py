from inventory.models import Tag
from django.shortcuts import get_object_or_404

Tag.objects.get(id=1) #Получение только одного объекта
Tag.objects.get_or_create(name="django-react") #Получение одного объекта, при отсутсвии создание его
get_object_or_404(Tag, name="django-react") #Получение одного объекта, при отсутсвии ошибка 404