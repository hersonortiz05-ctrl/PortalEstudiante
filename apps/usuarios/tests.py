from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, AnonymousUser
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import TestCase, RequestFactory, Client, override_settings
from django.urls import reverse
from django.views import View
from .permisos import SoloAdministradorMixin, SoloEstudianteMixin, es_administrador, es_estudiante
from .templatetags.roles import register


class VistaAdmin(SoloAdministradorMixin, View):
    def get(self, request):
        return HttpResponse('Administración')


class VistaEstudiante(SoloEstudianteMixin, View):
    def get(self, request):
        return HttpResponse('Estudiante')


@override_settings(SECURE_SSL_REDIRECT=False)
class PermisosTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Usuario=get_user_model()
        cls.estudiante=Usuario.objects.create_user(username='estudiante',password='Test-permisos!854')
        cls.admin=Usuario.objects.create_user(username='admin',password='Test-permisos!854')
        cls.sin_rol=Usuario.objects.create_user(username='sinrol',password='Test-permisos!854')
        grupo,_=Group.objects.get_or_create(name='Estudiante');cls.estudiante.groups.add(grupo)
        grupo,_=Group.objects.get_or_create(name='Administrador');cls.admin.groups.add(grupo)

    def solicitud(self, usuario):
        request=RequestFactory().get('/privado/')
        request.user=usuario
        return request

    def test_anonimo_va_a_login(self):
        self.assertEqual(VistaAdmin.as_view()(self.solicitud(AnonymousUser())).status_code,302)

    def test_estudiante_no_entra_en_admin_403(self):
        with self.assertRaises(PermissionDenied):
            VistaAdmin.as_view()(self.solicitud(self.estudiante))

    def test_admin_admitido_y_estudiante_admitido(self):
        self.assertEqual(VistaAdmin.as_view()(self.solicitud(self.admin)).status_code,200)
        self.assertEqual(VistaEstudiante.as_view()(self.solicitud(self.estudiante)).status_code,200)
        with self.assertRaises(PermissionDenied): VistaEstudiante.as_view()(self.solicitud(self.admin))
        with self.assertRaises(PermissionDenied): VistaEstudiante.as_view()(self.solicitud(self.sin_rol))

    def test_filtros_roles_y_usuario_inactivo(self):
        self.assertTrue(register.filters['es_estudiante'](self.estudiante))
        self.assertTrue(register.filters['es_administrador'](self.admin))
        self.estudiante.groups.add(Group.objects.get(name='Administrador'))
        self.assertFalse(es_estudiante(self.estudiante))
        self.admin.is_active=False
        self.assertFalse(es_administrador(self.admin))

    def test_login_valido_invalido_y_logout_post(self):
        self.assertContains(self.client.post(reverse('login'), {'username':'estudiante','password':'incorrecta'}),'Usuario o contraseña incorrectos')
        self.assertEqual(self.client.post(reverse('login'), {'username':'estudiante','password':'Test-permisos!854'}).status_code,302)
        self.assertEqual(self.client.get(reverse('logout')).status_code,405)
        self.assertEqual(self.client.post(reverse('logout')).status_code,302)
        self.assertEqual(self.client.get(reverse('dashboard')).status_code,302)

    def test_no_redireccion_externa(self):
        response=self.client.post(reverse('login'), {'username':'estudiante','password':'Test-permisos!854','next':'https://example.com/ajeno'})
        self.assertRedirects(response,reverse('dashboard'))

    def test_csrf_en_acceso_y_salida(self):
        cliente=Client(enforce_csrf_checks=True)
        self.assertEqual(cliente.post(reverse('login'),{'username':'estudiante','password':'Test-permisos!854'}).status_code,403)
        cliente.force_login(self.estudiante)
        self.assertEqual(cliente.post(reverse('logout')).status_code,403)
