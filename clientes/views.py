from django.shortcuts import render

from rest_framework import viewsets, generics, filters
from clientes.models import Clientes
from clientes.serializer import ClientesSerializer
from django_filters.rest_framework import DjangoFilterBackend



class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    filterset_fields = ['ativo']

class ListaClienteViewset(generics.ListAPIView):
    '''Lista um cliente especifico'''

    def get_queryset(self):
        queryset = Clientes.objects.filter(cliente_id=self.format_kwarg('pk'))
