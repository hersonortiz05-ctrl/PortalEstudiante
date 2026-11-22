from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.usuarios.urls')),
    path('', include('apps.principal.urls')),
    path('', include('apps.academico.urls')),
    path('', include('apps.avisos.urls')),
]
admin.site.site_header = 'Portal de Estudiantes · Administración'
admin.site.site_title = 'Portal de Estudiantes'
