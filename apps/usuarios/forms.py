from django.contrib.auth.forms import AuthenticationForm


class IngresoForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Usuario o contraseña incorrectos. Revisá tus datos.',
        'inactive': 'Tu cuenta está desactivada. Contactá a administración.',
    }
