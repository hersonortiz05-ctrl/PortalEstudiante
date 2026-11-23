from django import forms
from django.contrib import messages
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.usuarios.permisos import SoloAdministradorMixin


class ConfiguracionGestionMixin(SoloAdministradorMixin):
    entidad = ''
    titulo = ''
    columnas = ()
    campos_fila = ()
    campos_busqueda = ()

    def get_success_url(self):
        return reverse(f'{self.entidad}_lista')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto.update(titulo=self.titulo, url_cancelar=self.get_success_url())
        return contexto


class ListaGestionView(ConfiguracionGestionMixin, ListView):
    template_name = 'gestion/lista.html'
    paginate_by = 15

    def get_queryset(self):
        consulta = super().get_queryset()
        self.q = self.request.GET.get('q', '').strip()[:120]
        if self.q:
            condicion = Q()
            for campo in self.campos_busqueda:
                condicion |= Q(**{f'{campo}__icontains':self.q})
            consulta = consulta.filter(condicion)
        return consulta

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto.update(columnas=self.columnas, q=self.q, url_crear=reverse(f'{self.entidad}_crear'))
        contexto['filas'] = [
            {'objeto':objeto, 'valores':[str(getattr(objeto,campo)) for campo in self.campos_fila],
             'url_editar':reverse(f'{self.entidad}_editar',args=[objeto.pk]),
             'url_eliminar':reverse(f'{self.entidad}_eliminar',args=[objeto.pk])}
            for objeto in contexto['object_list']
        ]
        return contexto


class GuardarGestionMixin(ConfiguracionGestionMixin):
    template_name = 'gestion/form.html'

    def form_valid(self, form):
        try:
            with transaction.atomic():
                respuesta = super().form_valid(form)
        except IntegrityError:
            form.add_error(None, 'No se pudo guardar. Revisá duplicados y registros relacionados.')
            return self.form_invalid(form)
        messages.success(self.request, 'Registro guardado correctamente.')
        return respuesta


class CrearGestionView(GuardarGestionMixin, CreateView):
    pass


class EditarGestionView(GuardarGestionMixin, UpdateView):
    pass


class EliminarGestionView(ConfiguracionGestionMixin, DeleteView):
    template_name = 'gestion/confirmar_eliminar.html'
    context_object_name = 'objeto'

    def get_form_class(self):
        return forms.Form

    def form_valid(self, form):
        try:
            with transaction.atomic():
                self.object.delete()
        except ProtectedError:
            messages.error(self.request, 'No se puede eliminar: existen registros relacionados. Conservá su historial o revisá las dependencias con administración.')
            return redirect(self.get_success_url())
        messages.success(self.request, 'Registro eliminado correctamente.')
        return redirect(self.get_success_url())
