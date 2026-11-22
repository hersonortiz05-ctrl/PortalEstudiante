from django.contrib import admin
from .models import Carrera, Periodo, Curso, Estudiante, Matricula, Calificacion


@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre']
    search_fields = ['codigo', 'nombre']


@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_inicio', 'fecha_fin']
    search_fields = ['nombre']


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre']
    search_fields = ['codigo', 'nombre']


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'user', 'carrera', 'telefono']
    search_fields = ['codigo', 'user__username', 'user__first_name', 'user__last_name']
    list_filter = ['carrera']
    autocomplete_fields = ['user', 'carrera']


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['estudiante', 'curso', 'periodo']
    list_filter = ['periodo']
    search_fields = ['estudiante__codigo', 'curso__codigo', 'curso__nombre']
    autocomplete_fields = ['estudiante', 'curso', 'periodo']


@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ['matricula', 'nota', 'actualizada_en']
    search_fields = ['matricula__estudiante__codigo', 'matricula__curso__nombre']
    autocomplete_fields = ['matricula']
