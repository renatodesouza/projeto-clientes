
from django.contrib import admin
from django.urls import path, include

from clientes.views import ClientesViewSet, ListaClienteViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Clientes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cliente/<int:pk>/', ListaClienteViewset.as_view())
]
