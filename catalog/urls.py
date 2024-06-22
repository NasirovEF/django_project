from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ContactPageView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactPageView.as_view(), name="contacts"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("product_form/", ProductCreateView.as_view(), name="product_form"),
    path("product_update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path("product_delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),
]
