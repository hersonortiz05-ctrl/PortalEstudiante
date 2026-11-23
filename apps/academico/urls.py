from django.urls import path
from . import views

urlpatterns = [
    path('gestion/carreras/', views.CarreraListaView.as_view(), name='carrera_lista'),
    path('gestion/carreras/crear/', views.CarreraCrearView.as_view(), name='carrera_crear'),
    path('gestion/carreras/<int:pk>/editar/', views.CarreraEditarView.as_view(), name='carrera_editar'),
    path('gestion/carreras/<int:pk>/eliminar/', views.CarreraEliminarView.as_view(), name='carrera_eliminar'),
    path('gestion/periodos/', views.PeriodoListaView.as_view(), name='periodo_lista'),
    path('gestion/periodos/crear/', views.PeriodoCrearView.as_view(), name='periodo_crear'),
    path('gestion/periodos/<int:pk>/editar/', views.PeriodoEditarView.as_view(), name='periodo_editar'),
    path('gestion/periodos/<int:pk>/eliminar/', views.PeriodoEliminarView.as_view(), name='periodo_eliminar'),
    path('gestion/cursos/', views.CursoListaView.as_view(), name='curso_lista'),
    path('gestion/cursos/crear/', views.CursoCrearView.as_view(), name='curso_crear'),
    path('gestion/cursos/<int:pk>/editar/', views.CursoEditarView.as_view(), name='curso_editar'),
    path('gestion/cursos/<int:pk>/eliminar/', views.CursoEliminarView.as_view(), name='curso_eliminar'),
]
