from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ContactPageView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView, CategoryListView,
)
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("category_list/", CategoryListView.as_view(), name="category_list"),
    path("contacts/", ContactPageView.as_view(), name="contacts"),
    path("product/<int:pk>", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("product_form/", ProductCreateView.as_view(), name="product_form"),
    path("product_update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path("product_delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),
]
