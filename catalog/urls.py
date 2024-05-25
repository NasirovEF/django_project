from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, one_product, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product/<int:pk>", one_product, name="one_product"),
    path("add_product/", add_product, name="add_product"),
]
