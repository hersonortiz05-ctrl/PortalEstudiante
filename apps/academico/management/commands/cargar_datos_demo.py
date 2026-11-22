import os
from datetime import date, timedelta
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone
from apps.academico.models import Carrera, Periodo, Curso, Estudiante, Matricula, Calificacion
from apps.avisos.models import Aviso


class Command(BaseCommand):
    help = 'Carga datos ficticios idempotentes. La contraseña se lee de DEMO_PASSWORD.'

    @transaction.atomic
    def handle(self, *args, **options):
        clave = os.getenv('DEMO_PASSWORD', '')
        if not clave:
            raise CommandError('Configurá DEMO_PASSWORD en tu .env privado.')
        try:
            validate_password(clave)
        except ValidationError as error:
            raise CommandError('; '.join(error.messages)) from None
        estudiantes, _ = Group.objects.get_or_create(name='Estudiante')
        administradores, _ = Group.objects.get_or_create(name='Administrador')
        # Permite ejecutar este paquete antes del comando crear_grupos de Antonid.
        administradores.permissions.add(*Permission.objects.filter(content_type__app_label__in=['academico', 'avisos']))
        Usuario = get_user_model()
        admin, nuevo = Usuario.objects.get_or_create(username='demo.admin', defaults={'is_staff': True, 'email': 'admin@example.com', 'first_name': 'Administración', 'last_name': 'Demo'})
        if nuevo:
            admin.set_password(clave)
            admin.save()
            admin.groups.add(administradores)
        elif not admin.groups.filter(name='Administrador').exists():
            raise CommandError('demo.admin ya existe sin rol Administrador. No se modificó su acceso.')
        carreras = []
        for codigo, nombre in [('INF', 'Ingeniería en Infotecnología'), ('ADM', 'Administración de Empresas')]:
            obj, _ = Carrera.objects.get_or_create(codigo=codigo, defaults={'nombre': nombre})
            carreras.append(obj)
        periodos = []
        for nombre, inicio, fin in [('II período 2026', date(2026,5,1), date(2026,8,31)), ('III período 2026', date(2026,9,1), date(2026,12,20))]:
            obj, _ = Periodo.objects.get_or_create(nombre=nombre, defaults={'fecha_inicio': inicio, 'fecha_fin': fin})
            periodos.append(obj)
        cursos = []
        for codigo, nombre in [('WEB01','Desarrollo de Aplicaciones Web'), ('BD01','Bases de Datos'), ('RED01','Redes de Computadoras'), ('MAT01','Matemáticas')]:
            obj, _ = Curso.objects.get_or_create(codigo=codigo, defaults={'nombre':nombre, 'descripcion':'Curso ficticio para pruebas.'})
            cursos.append(obj)
        perfiles = []
        for indice, (usuario, nombre) in enumerate([('demo.ana','Ana'), ('demo.luis','Luis'), ('demo.sofia','Sofía')]):
            user, nuevo = Usuario.objects.get_or_create(username=usuario, defaults={'first_name': nombre, 'last_name':'Ejemplo', 'email': usuario+'@example.com'})
            if nuevo:
                user.set_password(clave)
                user.save()
                user.groups.add(estudiantes)
            elif not user.groups.filter(name='Estudiante').exists() or user.is_staff or user.is_superuser or user.groups.filter(name='Administrador').exists():
                raise CommandError(f'{usuario} existe con permisos distintos. No se modificó su acceso.')
            perfil, _ = Estudiante.objects.get_or_create(user=user, defaults={'codigo': f'DEMO00{indice+1}', 'carrera': carreras[indice % 2], 'telefono':'9999-0000', 'direccion':'Dirección ficticia'})
            perfiles.append(perfil)
        # Ana: cuatro matrículas con nota. Luis: dos sin nota. Sofía: sin matrícula.
        for indice, curso in enumerate(cursos):
            matricula, _ = Matricula.objects.get_or_create(estudiante=perfiles[0], curso=curso, periodo=periodos[1])
            Calificacion.objects.get_or_create(matricula=matricula, defaults={'nota':[85.50,92,0,100][indice], 'observacion':'Dato ficticio.'})
        for curso in cursos[:2]:
            Matricula.objects.get_or_create(estudiante=perfiles[1], curso=curso, periodo=periodos[0])
        ahora = timezone.now()
        ejemplos = [
            ('Bienvenida al período', None, True, ahora-timedelta(days=1), ahora+timedelta(days=30)),
            ('Actividad del curso de Redes', cursos[2], True, ahora-timedelta(days=1), ahora+timedelta(days=30)),
            ('Aviso vencido de demostración', None, True, ahora-timedelta(days=10), ahora-timedelta(days=1)),
            ('Borrador de demostración', None, False, ahora, None),
        ]
        for titulo, curso, publicado, inicio, fin in ejemplos:
            Aviso.objects.get_or_create(titulo=titulo, autor=admin, defaults={'curso':curso,'publicado':publicado,'fecha_publicacion':inicio,'fecha_fin':fin,'contenido':'Contenido ficticio para probar el portal.'})
        self.stdout.write(self.style.SUCCESS('Datos demo preparados. Usuarios: demo.admin, demo.ana, demo.luis, demo.sofia. Las contraseñas existentes no se cambian.'))
