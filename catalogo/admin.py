from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import ProductoModel


@admin.register(ProductoModel)
class ProductoAdmin(ImportExportModelAdmin):
    import_id_fields = ("id",)
    list_display = ("nombre", "precio", "stock", "usuario")
    search_fields = ("nombre",)
    list_filter = ("precio",)
    ordering = ("nombre",)
    list_per_page = 10

    readonly_fields = ("fecha_creacion", "fecha_modificacion", "usuario")

    fieldsets = (
        (
            "Información del Producto",
            {
                "fields": ("nombre", "descripcion", "precio", "stock", "imagen"),
                "classes": ("wide",),
            },
        ),
        (
            "Auditoría",
            {
                "fields": ("fecha_creacion", "fecha_modificacion", "usuario"),
                "classes": ("collapse",),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        return super().save_model(request, obj, form, change)
