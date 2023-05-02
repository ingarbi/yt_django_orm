from inventory.models import Product,Category, Brand
from django.db.models import Avg, Max, Count, Sum, Min

Product.objects.all()[:1] #start, stop, step/ первый элемент 
Product.objects.all().values("id", "name")[:3]# ввиде словаря
Product.objects.all().values_list("id", "name")[:3]# ввиде списка
Product.objects.order_by('name')# сортировка 
Product.objects.order_by('-id').values_list('id')# сортировка обратная
Product.objects.order_by('?')# сортировка рандомная
Product.objects.order_by('id').values_list('id').reverse().reverse()# сортировка обратная
Product.objects.all().first()# первый элемент
Product.objects.all().last()# последний элемент
Product.objects.all().earliest('time_create')# ранний элемент
Product.objects.all().latest('time_create')# последний элемент

Product.objects.aggregate(Avg('quantity')) #Средне кол-во всех
Product.objects.aggregate(average_q_ty=Avg('quantity'))#Средне кол-во всех используя собс переменную
Product.objects.filter(quantity__gt=15).aggregate(Sum('quantity'))#Сумма для прошедшего фильтр
Category.objects.filter(id=3).aggregate(Sum('products__quantity'))#Сумма через внешний ключ для прошедшего фильтр
Product.objects.aggregate(Max('quantity'), Min('quantity'))#Комбинирование нескольких агрегатов
x = Product.objects.annotate(num_q=Count('quantity'))#Аннотирование
x[0].num_q #Аннотирование возвращает переменную которую мы можем использовать
Product.objects.values('category').annotate(num_cat=Count('quantity'))#Аннотирование сколько категорий выбрано
Product.objects.values('category').annotate(num_cat=Sum('quantity'))#Аннотирование суммы для каждой категории


