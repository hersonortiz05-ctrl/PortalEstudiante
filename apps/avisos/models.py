from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q, F
from django.utils import timezone


class Aviso(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='autor')
    curso = models.ForeignKey('academico.Curso', on_delete=models.PROTECT, null=True, blank=True, related_name='avisos', verbose_name='curso')
    titulo = models.CharField('título', max_length=150)
    contenido = models.TextField('contenido')
    fecha_publicacion = models.DateTimeField('publicar desde', default=timezone.now)
    fecha_fin = models.DateTimeField('publicar hasta', null=True, blank=True)
    publicado = models.BooleanField('publicado', default=False)

    class Meta:
        ordering = ['-fecha_publicacion', '-pk']
        verbose_name = 'aviso'
        verbose_name_plural = 'avisos'
        constraints = [models.CheckConstraint(condition=Q(fecha_fin__isnull=True) | Q(fecha_fin__gte=F('fecha_publicacion')), name='aviso_fechas_validas')]

    def clean(self):
        if self.fecha_fin and self.fecha_publicacion and self.fecha_fin < self.fecha_publicacion:
            raise ValidationError({'fecha_fin': 'El cierre no puede ser anterior a la publicación.'})

    def __str__(self):
        return self.titulo
