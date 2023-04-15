from inventory.models import Brand
from django.db import connection, reset_queries

Brand.objects.create(brand_id=1, name="adidas")  # Создает объект
x = Brand.objects.all()  # ВОзвращает кверисет из данных
x = Brand.objects.all().delete()  # удаляет все данные
x = Brand.objects.all().query  # используется к кверисет чтобы увидеть запрос СКЬЮЭЛь
connection.queries  # Посмотреть все последние запросы скьэль
reset_queries()  # очистить все последние запросы скьэль

cursor = connection.cursor()
cursor.execute("INSERT INTO inventory_brand (brand_id, name) VALUES (%s, %s)", ['1', "addidas"]) #raw sql query

x = Brand.objects.filter(brand_id=1)  # Фильтр по определенным параматрам
x = Brand.objects.all().count()  # Подсчет вернувшихся объектов
len(x)  # Подсчет вернувшихся объектов

for i in x:
    print(i.brand_id)

Brand.objects.all().values()  # Возвращат данные в виде словаря
Brand.objects.all().values(
    "name"
)  # Возвращат данные в виде словаря по определенным параматрам

Brand.objects.save(
    brand_id=1, name="adidas"
)  # Сохраняет обновляя если есть такая запись, в противном случае создает новую
