from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsCreateView, ProductDeleteView, ProductUpdateView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', ProductListView.as_view(), name='home'),
    path('', ContactsCreateView.as_view(), name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('view/<int:pk>/', cache_page(10)(ProductDetailView.as_view()), name='view'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]
