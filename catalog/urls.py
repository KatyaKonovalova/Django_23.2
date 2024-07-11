from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [path("", home, name="home"),
               path("contacts/", contacts, name="contacts"),
               path("products_list/", ProductListView.as_view(), name="products_list"),
               path("products_detail/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
               path("products/create", ProductCreateView.as_view(), name="products_create"),
               path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"),
               path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_delete"),]
