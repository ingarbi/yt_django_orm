from inventory.models import Brand

Brand.objects.create(brand_id=1, name="adidas")  # Создает объект

x = Brand.objects.all()  # ВОзвращает кверисет из данных

x = Brand.objects.all().query  # используется к кверисет чтобы увидеть запрос СКЬЮЭЛь
