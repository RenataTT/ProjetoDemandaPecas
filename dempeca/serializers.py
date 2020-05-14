from rest_framework import serializers
from .models import *

class PecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peca 
        fields = ('idPeca', 'valor', 'descricao')
    pass 

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario 
        fields = ('idUsuario', 'nome')
    pass 

class DemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demanda 
        fields = ('idDemanda', 'rua', 'bairro', 'numero', 'cidade', 'cep', 'status', 'usuario', 'pecas')
    pass 