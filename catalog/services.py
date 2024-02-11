from django.conf import settings

from catalog.models import Product
from django.core.cache import cache



def get_cached_product_list():
    key = 'product_list'
    queryset = Product.objects.all()
    if settings.LOW_CACHED:
        product_list = cache.get(key)
        if product_list is None:
            product_list = queryset
            cache.set(key, product_list)
        return product_list
    return queryset