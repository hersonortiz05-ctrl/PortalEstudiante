from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def es_administrador(usuario):
    return bool(usuario.is_authenticated and usuario.is_active and (
        usuario.is_superuser or usuario.groups.filter(name='Administrador').exists()
    ))


def es_estudiante(usuario):
    # Si una cuenta tiene ambos grupos, prevalece Administrador.
    return bool(usuario.is_authenticated and usuario.is_active and not es_administrador(usuario)
                and usuario.groups.filter(name='Estudiante').exists())


class SoloAdministradorMixin(LoginRequiredMixin, UserPassesTestMixin):
    permission_denied_message = 'Solo administración puede acceder a esta sección.'

    def test_func(self):
        return es_administrador(self.request.user)


class SoloEstudianteMixin(LoginRequiredMixin, UserPassesTestMixin):
    permission_denied_message = 'Esta sección es exclusiva para estudiantes.'

    def test_func(self):
        return es_estudiante(self.request.user)
