from django import template
from apps.usuarios.permisos import es_administrador, es_estudiante

register = template.Library()
register.filter('es_administrador', es_administrador)
register.filter('es_estudiante', es_estudiante)
