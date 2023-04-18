from inventory.models import Brand, Category, Tag, Stock
from django.db import connection, reset_queries

Brand.objects.create(brand_id=1, name="adidas", category_id=1)  # Создает объект
Category.objects.create(name="T-shirts")  # Создает объект
x = Brand.objects.all()  # ВОзвращает кверисет из данных
x = Brand.objects.all().delete()  # удаляет все данные
x = Brand.objects.all().query  # используется к кверисет чтобы увидеть запрос СКЬЮЭЛь
connection.queries  # Посмотреть все последние запросы скьэль
reset_queries()  # очистить все последние запросы скьэль

cursor = connection.cursor()
cursor.execute(
    "INSERT INTO inventory_brand (brand_id, name) VALUES (%s, %s)", ["1", "addidas"]
)  # raw sql query

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

x = Brand.objects.get(brand_id=222)  # Получение определнного объекта
x.tag.add(Tag.objects.get(id=2))  # Добавление определнного тега к объекту
x.tag.remove(Tag.objects.get(id=2))  # Удаление определнного тега объекта
x.tag.add(Tag.objects.create(name="new"))  # Добавление тега к объекту СОЗДАНИЕМ

Stock.objects.update(quantity=11, product_brand_id=222)  # Обновление данных


data = [
    {"brand_id": 9, "name": "adidas-9", "category_id": 1},
    {"brand_id": 11, "name": "adidas-11", "category_id": 1},
]
Brand.objects.bulk_create([Brand(**abc) for abc in data]) #Создание много записей через упаковку словаря

Brand.objects.bulk_create(
    [
        Brand(brand_id=4, name="adidas-4", category_id=1),
        Brand(brand_id=5, name="adidas-5", category_id=2),
        Brand(brand_id=6, name="adidas-6", category_id=1),
    ]
)  ##Создание много записей
