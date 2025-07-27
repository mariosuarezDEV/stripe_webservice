from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Auditoria(models.Model):
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación", auto_created=True)
    fecha_modificacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de modificación")
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Usuario", related_name="%(class)s_auditorias", help_text="Usuario que realizó la acción")

    class Meta:
        verbose_name = "Auditoría"
        verbose_name_plural = "Auditorías"
        abstract = True  # Quiere decir que no se crea el modelo en BD, sino que se utiliza como base para otros modelos
