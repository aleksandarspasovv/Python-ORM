from django.db import models


class ProductManager(models.Manager):

    def available_products(self):
        return self.filter(is_avaliable=True)

    def available_products_in_category(self, category_name: str):
        return self.filter(is_avaliable=True, category__name=category_name)
