from django.urls import path
from .views import ProductoListView, ProductoCreate

urlpatterns = [
    path("", ProductoListView.as_view(), name="producto_list"),
    path("nuevo/", ProductoCreate.as_view(), name="producto_create"),
]
