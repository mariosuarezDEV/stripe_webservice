from django.urls import path, include
from .views import (
    SuccessView,
    ErrorView,
    CreateCheckoutSessionProductoView,
)

urlpatterns = [
    path(
        "success/",
        SuccessView.as_view(),
        name="success",
    ),
    path(
        "error/",
        ErrorView.as_view(),
        name="error",
    ),
    path(
        "comprar/<int:producto_id>/",
        CreateCheckoutSessionProductoView.as_view(),
        name="comprar_producto",
    ),
]
