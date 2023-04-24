from inventory.models import Tag, Category, Brand, Stock
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

Brand.objects.filter(category_id__name="Python") #переход в таблицу Категория
Brand.objects.filter(category_id__name__contains="p")# переход в таблицу Категория + поиск по фильтру
first_brand = Category.objects.first()# Первый объект в таблице
first_brand.brand_set.all()# Без оелайтед нейм
first_brand.brands.all()# С использованием релайтед нейм

Stock.objects.filter(product_brand__name__contains='adi')# Достаем нейм из Брэнд таблицы
Brand.objects.filter(stock_brand__quantity__lte=3)# # Достаем кол-во из Сток таблицы через релайтед нейм
Brand.objects.filter(stock_brand__quantity__gte=3)# Достаем кол-во из Сток таблицы через релайтед нейм

Brand.objects.filter(tag__id=1)
Brand.objects.filter(tag__name__contains="re")
Brand.tag.through.objects.all()
Tag.objects.filter(brand_tags__brand_id=1)
Tag.objects.filter(brand_tags__brand_id__gte=1)
