from datetime import date
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase, Client, override_settings
from django.urls import reverse
from .models import Carrera, Periodo, Curso, Estudiante, Matricula


@override_settings(SECURE_SSL_REDIRECT=False)
class CatalogosTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin=get_user_model().objects.create_user(username='gestor')
        grupo,_=Group.objects.get_or_create(name='Administrador');cls.admin.groups.add(grupo)
        cls.usuario=get_user_model().objects.create_user(username='alumno')
        grupo,_=Group.objects.get_or_create(name='Estudiante');cls.usuario.groups.add(grupo)

    def test_crud_tres_catalogos(self):
        self.client.force_login(self.admin)
        casos=[('carrera',Carrera,{'codigo':'TEST','nombre':'Carrera'}),('periodo',Periodo,{'nombre':'Período','fecha_inicio':'2026-01-01','fecha_fin':'2026-04-01'}),('curso',Curso,{'codigo':'TEST','nombre':'Curso','descripcion':'Prueba'})]
        for entidad,modelo,datos in casos:
            with self.subTest(entidad=entidad):
                self.assertEqual(self.client.get(reverse(entidad+'_crear')).status_code,200)
                self.assertEqual(self.client.post(reverse(entidad+'_crear'),datos).status_code,302)
                objeto=modelo.objects.get()
                self.assertContains(self.client.get(reverse(entidad+'_lista')),datos['nombre'])
                datos['nombre']='Editado'
                self.assertEqual(self.client.post(reverse(entidad+'_editar',args=[objeto.pk]),datos).status_code,302)
                objeto.refresh_from_db();self.assertEqual(objeto.nombre,'Editado')
                self.assertEqual(self.client.get(reverse(entidad+'_eliminar',args=[objeto.pk])).status_code,200)
                self.assertEqual(self.client.post(reverse(entidad+'_eliminar',args=[objeto.pk]),{}).status_code,302)
                self.assertEqual(modelo.objects.count(),0)

    def test_estudiante_recibe_403_en_todas_las_operaciones(self):
        self.client.force_login(self.usuario)
        for entidad in ['carrera','periodo','curso']:
            for accion in ['lista','crear','editar','eliminar']:
                url=reverse(entidad+'_'+accion,args=[999] if accion in ['editar','eliminar'] else [])
                self.assertEqual(self.client.get(url).status_code,403)
                self.assertEqual(self.client.post(url,{}).status_code,403)

    def test_validaciones_y_busqueda(self):
        self.client.force_login(self.admin)
        Curso.objects.create(codigo='WEB',nombre='Desarrollo Web')
        response=self.client.post(reverse('curso_crear'),{'codigo':'WEB','nombre':'Duplicado'})
        self.assertEqual(response.status_code,200);self.assertIn('codigo',response.context['form'].errors)
        response=self.client.post(reverse('curso_crear'),{'codigo':'','nombre':''})
        self.assertTrue(response.context['form'].errors)
        response=self.client.post(reverse('periodo_crear'),{'nombre':'Mal','fecha_inicio':'2026-12-01','fecha_fin':'2026-01-01'})
        self.assertIn('fecha_fin',response.context['form'].errors)
        self.assertContains(self.client.get(reverse('curso_lista'),{'q':'WEB'}),'Desarrollo Web')
        self.assertNotContains(self.client.get(reverse('curso_lista'),{'q':'ausente'}),'Desarrollo Web')

    def test_eliminar_relacionado_muestra_mensaje(self):
        carrera=Carrera.objects.create(codigo='INF',nombre='Informática')
        estudiante=Estudiante.objects.create(user=self.usuario,carrera=carrera,codigo='001')
        periodo=Periodo.objects.create(nombre='III',fecha_inicio=date(2026,9,1),fecha_fin=date(2026,12,1))
        curso=Curso.objects.create(codigo='WEB',nombre='Web')
        Matricula.objects.create(estudiante=estudiante,curso=curso,periodo=periodo)
        self.client.force_login(self.admin)
        response=self.client.post(reverse('curso_eliminar',args=[curso.pk]),{},follow=True)
        self.assertContains(response,'existen registros relacionados')
        self.assertTrue(Curso.objects.filter(pk=curso.pk).exists())

    def test_csrf_exigido(self):
        cliente=Client(enforce_csrf_checks=True);cliente.force_login(self.admin)
        self.assertEqual(cliente.post(reverse('curso_crear'),{'codigo':'CSRF','nombre':'No guardar'}).status_code,403)
        self.assertFalse(Curso.objects.exists())

    def test_paginacion(self):
        Curso.objects.bulk_create([Curso(codigo=f'C{i:02}',nombre=f'Curso {i}') for i in range(18)])
        self.client.force_login(self.admin)
        respuesta=self.client.get(reverse('curso_lista'),{'page':2})
        self.assertEqual(len(respuesta.context['filas']),3)
