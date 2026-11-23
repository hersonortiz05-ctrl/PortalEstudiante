from django.urls import path
from .views import IngresoView, SalidaView

urlpatterns = [
    path('login/', IngresoView.as_view(), name='login'),
    path('logout/', SalidaView.as_view(), name='logout'),
]
