from inventory.models import Product

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