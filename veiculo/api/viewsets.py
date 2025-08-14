from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
# from livros.models import Livro
from veiculo.api import serializers
from veiculo import models
from rest_framework.permissions import IsAuthenticated


class VeiculoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
        
    serializer_class = serializers.VeiculoSerializers
    queryset = models.Veiculo.objects.all()
    pagination_class = PageNumberPagination