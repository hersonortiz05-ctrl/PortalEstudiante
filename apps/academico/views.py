from .models import Carrera, Periodo, Curso
from .forms import CarreraForm, PeriodoForm, CursoForm
from .gestion import ListaGestionView, CrearGestionView, EditarGestionView, EliminarGestionView


class CarreraConfig:
    model = Carrera
    form_class = CarreraForm
    entidad = 'carrera'
    titulo = 'Carreras'
    columnas = ('Código', 'Nombre')
    campos_fila = ('codigo', 'nombre')
    campos_busqueda = ('codigo', 'nombre')


class PeriodoConfig:
    model = Periodo
    form_class = PeriodoForm
    entidad = 'periodo'
    titulo = 'Períodos'
    columnas = ('Nombre', 'Inicio', 'Cierre')
    campos_fila = ('nombre', 'fecha_inicio', 'fecha_fin')
    campos_busqueda = ('nombre',)


class CursoConfig:
    model = Curso
    form_class = CursoForm
    entidad = 'curso'
    titulo = 'Cursos'
    columnas = ('Código', 'Nombre')
    campos_fila = ('codigo', 'nombre')
    campos_busqueda = ('codigo', 'nombre')


class CarreraListaView(CarreraConfig, ListaGestionView):
    pass
class CarreraCrearView(CarreraConfig, CrearGestionView):
    pass
class CarreraEditarView(CarreraConfig, EditarGestionView):
    pass
class CarreraEliminarView(CarreraConfig, EliminarGestionView):
    pass
class PeriodoListaView(PeriodoConfig, ListaGestionView):
    pass
class PeriodoCrearView(PeriodoConfig, CrearGestionView):
    pass
class PeriodoEditarView(PeriodoConfig, EditarGestionView):
    pass
class PeriodoEliminarView(PeriodoConfig, EliminarGestionView):
    pass
class CursoListaView(CursoConfig, ListaGestionView):
    pass
class CursoCrearView(CursoConfig, CrearGestionView):
    pass
class CursoEditarView(CursoConfig, EditarGestionView):
    pass
class CursoEliminarView(CursoConfig, EliminarGestionView):
    pass
