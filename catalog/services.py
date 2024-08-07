from catalog.models import Category
from config.settings import CACHE_ENABLED
from django.core.cache import cache


def get_category_from_cache():
    if CACHE_ENABLED:
        key = f'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list
