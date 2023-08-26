from rest_framework import serializers
from apps.ecommerce.models import * 


class AdministradorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Administrador
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        exclude = ['data_de_registro']