from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from empresa.api import serializers
from empresa import models


class EmpresaViewSet(viewsets.ModelViewSet):
    persmision_classes = [IsAuthenticated]
    
    serializer_class = serializers.EmpresaSerializers
    queryset = models.Empresa.objects.all()