from django.conf import settings

from catalog.models import Product
from django.core.cache import cache


def get_cached_product_list(product_pk):

    if settings.LOW_CACHED:
        key = f'{product_pk}'
        product_list = cache.get(key)

        if product_list is None:
            product_list = Product.objects.all()
            cache.set(key, product_list)
        else:
            product_list = Product.objects.all()

        return product_list
