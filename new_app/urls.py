from django.urls import path
from .views import add_product, search_products

urlpatterns = [
    path('add/', add_product, name='add_product'),
    path('search/', search_products, name='search_products'),
]
