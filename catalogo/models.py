from django.db import models
from bases.models import Auditoria

# Create your models here.


class ProductoModel(Auditoria):
    nombre = models.CharField(
        max_length=100,
        help_text="Nombre con el que producto será visualizado",
        blank=False,
        null=False,
        verbose_name="Nombre del producto",
    )
    descripcion = models.TextField(
        help_text="Descripción del producto",
        blank=True,
        null=True,
        verbose_name="Descripción del producto",
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Precio del producto",
        blank=False,
        null=False,
        verbose_name="Precio del producto",
    )
    stock = models.PositiveIntegerField(
        help_text="Cantidad de producto disponible",
        blank=False,
        null=False,
        verbose_name="Stock del producto",
    )
    imagen = models.ImageField(
        upload_to="productos/",
        help_text="Imagen del producto",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "productos"
        managed = True
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
