from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Q, F


class Carrera(models.Model):
    codigo = models.CharField('código', max_length=20, unique=True)
    nombre = models.CharField('nombre', max_length=120)

    class Meta:
        ordering = ['nombre', 'pk']
        verbose_name = 'carrera'
        verbose_name_plural = 'carreras'

    def __str__(self):
        return self.nombre


class Periodo(models.Model):
    nombre = models.CharField('nombre', max_length=60, unique=True)
    fecha_inicio = models.DateField('fecha de inicio')
    fecha_fin = models.DateField('fecha de cierre')

    class Meta:
        ordering = ['-fecha_inicio', '-pk']
        verbose_name = 'período'
        verbose_name_plural = 'períodos'
        constraints = [models.CheckConstraint(condition=Q(fecha_fin__gte=F('fecha_inicio')), name='periodo_fechas_validas')]

    def clean(self):
        if self.fecha_inicio and self.fecha_fin and self.fecha_fin < self.fecha_inicio:
            raise ValidationError({'fecha_fin': 'El cierre no puede ser anterior al inicio.'})

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    codigo = models.CharField('código', max_length=20, unique=True)
    nombre = models.CharField('nombre', max_length=120)
    descripcion = models.TextField('descripción', blank=True)

    class Meta:
        ordering = ['codigo', 'pk']
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

    def __str__(self):
        return f'{self.codigo} · {self.nombre}'


class Estudiante(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='estudiante', verbose_name='usuario')
    carrera = models.ForeignKey(Carrera, on_delete=models.PROTECT, related_name='estudiantes', verbose_name='carrera')
    codigo = models.CharField('número de cuenta', max_length=20, unique=True)
    telefono = models.CharField('teléfono', max_length=25, blank=True)
    direccion = models.CharField('dirección', max_length=200, blank=True)

    class Meta:
        ordering = ['codigo', 'pk']
        verbose_name = 'estudiante'
        verbose_name_plural = 'estudiantes'

    def __str__(self):
        return f'{self.codigo} · {self.user.get_full_name() or self.user.username}'


class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT, related_name='matriculas', verbose_name='estudiante')
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name='matriculas', verbose_name='curso')
    periodo = models.ForeignKey(Periodo, on_delete=models.PROTECT, related_name='matriculas', verbose_name='período')
    fecha_registro = models.DateTimeField('fecha de registro', auto_now_add=True)

    class Meta:
        ordering = ['-periodo__fecha_inicio', 'curso__codigo', 'pk']
        verbose_name = 'matrícula'
        verbose_name_plural = 'matrículas'
        constraints = [models.UniqueConstraint(fields=['estudiante', 'curso', 'periodo'], name='matricula_unica')]

    def __str__(self):
        return f'{self.estudiante} / {self.curso} / {self.periodo}'


class Calificacion(models.Model):
    matricula = models.OneToOneField(Matricula, on_delete=models.PROTECT, related_name='calificacion', verbose_name='matrícula')
    nota = models.DecimalField('nota', max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    observacion = models.CharField('observación', max_length=250, blank=True)
    actualizada_en = models.DateTimeField('actualizada', auto_now=True)

    class Meta:
        verbose_name = 'calificación'
        verbose_name_plural = 'calificaciones'
        constraints = [models.CheckConstraint(condition=Q(nota__gte=0, nota__lte=100), name='calificacion_rango_valido')]

    def __str__(self):
        return f'{self.matricula} · {self.nota}'
