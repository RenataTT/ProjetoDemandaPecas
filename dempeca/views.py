from django.shortcuts import render
from  . import models 
from .serializers import *
from rest_framework import viewsets, authentication, permissions, reverse, serializers


# Create your views here.
class DemandaViewSet(viewsets.ModelViewSet):
    queryset = Demanda.objects.order_by('idDemanda')
    serializer_class = DemandaSerializer
    links = serializers.SerializerMethodField() 

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse ('demanda-detail', kwarg={'pk': obj.pk}, request=request )
        }
        pass
    pass

class PecaViewSet(viewsets.ModelViewSet):
    queryset = Peca.objects.order_by('valor')
    serializer_class = PecaSerializer
    links = serializers.SerializerMethodField() 

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse ('peca-detail', kwarg={'pk': obj.pk}, request=request )
        }
        pass
    pass

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.order_by('nome')
    serializer_class = UsuarioSerializer
    links = serializers.SerializerMethodField() 

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse ('usuario-detail', kwarg={'pk': obj.pk}, request=request )
        }
        pass
    pass

# class DefaultsMixin(object):
#     authentication_classes = (
#         authentication.BasicAuthentication,
#         authentication.TokenAthentication
#     )
#     permission_classes = (
#         permissions.IsAuthenticated
#     )
#     pass 


