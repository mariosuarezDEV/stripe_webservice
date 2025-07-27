from django.views.generic import ListView, CreateView
from .models import ProductoModel
from .forms import ProductoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


class ProductoListView(ListView):
    model = ProductoModel
    template_name = "productos.html"
    context_object_name = "productos"


class ProductoCreate(CreateView):
    model = ProductoModel
    form_class = ProductoForm
    template_name = "crear_producto.html"
    success_url = reverse_lazy("producto_list")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
