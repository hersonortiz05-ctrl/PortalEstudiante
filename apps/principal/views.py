from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView
from apps.academico.models import Estudiante, Matricula


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'principal/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        # Esta base funciona antes de aplicar el módulo de permisos de Antonid.
        grupos = set(usuario.groups.values_list('name', flat=True))
        administrador = usuario.is_superuser or 'Administrador' in grupos
        if not administrador and 'Estudiante' not in grupos:
            raise PermissionDenied('Tu cuenta no tiene un rol asignado. Contactá a administración.')
        context['es_admin'] = administrador
        context['nombre_usuario'] = usuario.get_full_name() or usuario.username
        if administrador:
            context['total_estudiantes'] = Estudiante.objects.count()
            context['total_matriculas'] = Matricula.objects.count()
        else:
            context['estudiante'] = Estudiante.objects.select_related('carrera').filter(user=usuario).first()
            context['matriculas'] = Matricula.objects.filter(estudiante__user=usuario).select_related('curso', 'periodo')
        return context
