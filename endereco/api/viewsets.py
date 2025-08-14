from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
# from livros.models import Livro
from endereco.api import serializers
from endereco import models
from rest_framework.permissions import IsAuthenticated


class EnderecoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
        
    serializer_class = serializers.EnderecoSerializers
    queryset = models.Endereco.objects.all()
    pagination_class = PageNumberPagination
    