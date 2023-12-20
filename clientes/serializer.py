from rest_framework import serializers

from clientes.models import Clientes
from clientes.validadores import cpf_valido, nome_valido, rg_valido, celular_valido



class ClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clientes
        fields = '__all__'

    def validadores(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "CPF deve ter 11 digitos"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'Este campo é permitido apenas letras'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'O campo RG esta incorreto'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"Número ou formato de celular invalido"})


class ListaClienteSerializer(serializers.ModelSerializer):
    cliente = serializers.ReadOnlyField(source='cliente.nome')

    class Meta:
        models= Clientes
        fields = ['cliente']