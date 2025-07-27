# views.py
import stripe
from django.conf import settings
from django.views.generic import View, TemplateView
from django.urls import reverse_lazy
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from catalogo.models import ProductoModel
from django.shortcuts import redirect


@method_decorator(csrf_exempt, name="dispatch")
class CreateCheckoutSessionProductoView(View):

    def get(self, request, *args, **kwargs):
        producto_id = kwargs.get("producto_id")
        producto = ProductoModel.objects.get(id=producto_id)

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "mxn",
                        "unit_amount": int(producto.precio * 100),
                        "product_data": {
                            "name": producto.nombre,
                            "images": (
                                [request.build_absolute_uri(producto.imagen.url)]
                                if producto.imagen
                                else []
                            ),
                        },
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=request.build_absolute_uri(reverse_lazy("success")),
            cancel_url=request.build_absolute_uri(reverse_lazy("error")),
        )
        return redirect(session.url)  # <-- Redirige directo a Stripe


class SuccessView(TemplateView):
    template_name = "success.html"


class ErrorView(TemplateView):
    template_name = "error.html"
