import json

from django.core.management import BaseCommand
from catalog.models import Category, Product

data_category = 'data_category.json'
data_product = 'data_product.json'


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """Метод получения данных из фикстуры с категориями"""
        categories_list = []
        with open(data_category, encoding='utf-16') as file:
            categories = json.load(file)
            for cat in categories:
                categories_list.append(Category(**cat.get('fields')))
        return categories_list

    @staticmethod
    def json_read_products():
        """Метод получения данных из фикстуры с продуктами"""
        products_list = []
        with open(data_product, encoding='utf-16') as file:
            products = json.load(file)
            for prod in products:
                products_list.append(Product(**prod.get('fields')))
        return products_list

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.bulk_create(self.json_read_categories())
        Product.objects.bulk_create(self.json_read_products())
