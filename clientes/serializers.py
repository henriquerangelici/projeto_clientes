from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
             raise serializers.ValidationError({'cpf':"Numero de CPF invalido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não põe numeros, zé mane"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"RG tem que ter 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"Celular tem que seguir: 11 91234-1234"})


        return data


   