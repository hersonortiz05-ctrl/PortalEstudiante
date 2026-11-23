from django.contrib.auth.views import LoginView, LogoutView
from .forms import IngresoForm


class IngresoView(LoginView):
    template_name = 'usuarios/login.html'
    authentication_form = IngresoForm
    redirect_authenticated_user = True


class SalidaView(LogoutView):
    http_method_names = ['post', 'options']
