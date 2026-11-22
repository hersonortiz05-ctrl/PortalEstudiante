from django.contrib import admin
from .models import Aviso


@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'curso', 'publicado', 'fecha_publicacion', 'fecha_fin']
    search_fields = ['titulo', 'contenido']
    list_filter = ['publicado', 'curso']
    autocomplete_fields = ['curso']

    def save_model(self, request, obj, form, change):
        if not obj.autor_id:
            obj.autor = request.user
        super().save_model(request, obj, form, change)
