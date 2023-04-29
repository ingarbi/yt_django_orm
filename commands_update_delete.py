from inventory.models import Tag, Category, Brand, Stock


Brand.objects.filter(brand_id=1).update(name="new name")# обновление имени по айди
Brand.objects.update_or_create(name="new name")# обновление имени использовать с дефолтс
Tag.objects.update_or_create(name="new name")# обновление имени использовать с дефолтс
Tag.objects.update_or_create(name="new name", defaults={"name":"old name"})# обновление имени

# bulk_update(objs, fields, batch_size=None)

objs = [ Tag.objects.get(id=6), Tag.objects.get(id=7),]
objs[0].name = ["old old name"]
objs[1].name = ["new new name2"]

Tag.objects.bulk_update(objs, ['name']) # обновление имени для многих записей

Brand.objects.all().delete()#Удаление всех данных
Brand.objects.filter(brand_id=1).delete()#Удаление по айди
Stock.objects.filter(id=4).delete()#Удаление по айди