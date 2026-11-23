from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = 'Crea los grupos del portal. Ejecutar después de migrate.'

    @transaction.atomic
    def handle(self, *args, **options):
        estudiante, _ = Group.objects.get_or_create(name='Estudiante')
        administrador, _ = Group.objects.get_or_create(name='Administrador')
        # No dar permisos globales de modelo al estudiante: consulta solo sus datos.
        estudiante.permissions.clear()
        permisos = Permission.objects.filter(content_type__app_label__in=['academico', 'avisos'])
        administrador.permissions.add(*permisos)
        self.stdout.write(self.style.SUCCESS('Grupos Estudiante y Administrador preparados. No se modificaron cuentas.'))
