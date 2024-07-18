from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLE


def get_products_from_cache():
    """Получает данные по продуктам из кэша, если кэш пуст, получает данные из бд"""
    if not CACHE_ENABLE:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    cache.set(key, products)
    return products
