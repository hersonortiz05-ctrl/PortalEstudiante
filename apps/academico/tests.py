from datetime import date, timedelta
from decimal import Decimal
from io import StringIO
import os
from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.management import call_command
from django.db import IntegrityError, transaction
from django.db.models.deletion import ProtectedError
from django.test import TestCase
from django.utils import timezone
from .models import Carrera, Periodo, Curso, Estudiante, Matricula, Calificacion
from apps.avisos.models import Aviso


class ModelosTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='modelo')
        cls.carrera = Carrera.objects.create(codigo='INF', nombre='Informática')
        cls.periodo = Periodo.objects.create(nombre='III', fecha_inicio=date(2026,9,1), fecha_fin=date(2026,12,20))
        cls.curso = Curso.objects.create(codigo='WEB', nombre='Web')
        cls.estudiante = Estudiante.objects.create(user=cls.user, carrera=cls.carrera, codigo='001')
        cls.matricula = Matricula.objects.create(estudiante=cls.estudiante,curso=cls.curso,periodo=cls.periodo)

    def test_tablas_del_contrato(self):
        for modelo, tabla in [(Carrera,'academico_carrera'),(Periodo,'academico_periodo'),(Curso,'academico_curso'),(Estudiante,'academico_estudiante'),(Matricula,'academico_matricula'),(Calificacion,'academico_calificacion'),(Aviso,'avisos_aviso')]:
            self.assertEqual(modelo._meta.db_table,tabla)

    def test_matricula_duplicada(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            Matricula.objects.create(estudiante=self.estudiante,curso=self.curso,periodo=self.periodo)

    def test_notas_limites_validacion_y_sql(self):
        for nota in [-1,101]:
            calificacion=Calificacion(matricula=self.matricula,nota=nota)
            with self.assertRaises(ValidationError): calificacion.full_clean()
            with self.assertRaises(IntegrityError), transaction.atomic(): calificacion.save()
        for nota in [0,100,Decimal('85.50')]:
            Calificacion.objects.update_or_create(matricula=self.matricula, defaults={'nota':nota})
            self.assertEqual(Calificacion.objects.get(matricula=self.matricula).nota,nota)

    def test_fechas_y_relaciones(self):
        self.periodo.fecha_fin=date(2026,1,1)
        with self.assertRaises(ValidationError): self.periodo.full_clean()
        with self.assertRaises(IntegrityError), transaction.atomic(): self.periodo.save()
        with self.assertRaises(ProtectedError): self.curso.delete()
        with self.assertRaises(ProtectedError): self.user.delete()

    def test_aviso_fecha_fin_igual_permitida(self):
        ahora=timezone.now()
        aviso=Aviso(autor=self.user,titulo='Válido',contenido='Texto',fecha_publicacion=ahora,fecha_fin=ahora)
        aviso.full_clean();aviso.save()
        aviso.fecha_fin=ahora-timedelta(seconds=1)
        with self.assertRaises(ValidationError): aviso.full_clean()
        with self.assertRaises(IntegrityError),transaction.atomic(): aviso.save()


class DatosDemoTests(TestCase):
    def test_conteos_y_repeticion(self):
        with patch.dict(os.environ,{'DEMO_PASSWORD':'Clave-solo-test!854'}):
            call_command('cargar_datos_demo',stdout=StringIO())
            modelos=[get_user_model(),Carrera,Periodo,Curso,Estudiante,Matricula,Calificacion,Aviso]
            self.assertEqual([m.objects.count() for m in modelos],[4,2,2,4,3,6,4,4])
            clave=get_user_model().objects.get(username='demo.ana').password
            call_command('cargar_datos_demo',stdout=StringIO())
            self.assertEqual([m.objects.count() for m in modelos],[4,2,2,4,3,6,4,4])
            self.assertEqual(get_user_model().objects.get(username='demo.ana').password,clave)
            self.assertFalse(Estudiante.objects.get(user__username='demo.sofia').matriculas.exists())
            self.assertFalse(Calificacion.objects.filter(matricula__estudiante__user__username='demo.luis').exists())
