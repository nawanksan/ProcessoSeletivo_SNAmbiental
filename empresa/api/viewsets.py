from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from empresa.api import serializers
from empresa import models
from veiculo.models import Veiculo
from rest_framework.response import Response
from rest_framework.decorators import action
from empresa.models import Empresa
from veiculo.api.serializers import VeiculoSerializers
from endereco.api.serializers import EnderecoSerializers


class EmpresaViewSet(viewsets.ModelViewSet):
    persmision_classes = [IsAuthenticated]
    
    serializer_class = serializers.EmpresaSerializers
    queryset = models.Empresa.objects.all()
    pagination_class = PageNumberPagination
    
    
     # II Consultar por CNPJ
    @action(detail=False, methods=['get'], url_path='cnpj/(?P<cnpj>[^/.]+)')
    def consultar_por_cnpj(self, request, cnpj=None):
        empresa = Empresa.objects.filter(vCnpj=cnpj).first()
        if empresa:
            return Response(self.get_serializer(empresa).data)
        return Response({"detail": "Empresa não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    # III consultar por ID com os veículos
    @action(detail=True, methods=['get'], url_path='com-veiculos')
    def consultar_com_veiculos(self, request, pk=None):
        empresa = self.get_object()
        data = self.get_serializer(empresa).data
        data['veiculos']=VeiculoSerializers(Veiculo.objects.filter(iCod_empresa=empresa), many=True).data
        return Response(data)
    
    
    # IV consultar por ID ou CNPJ com endereço completo
    @action(detail=False, methods=['get'], url_path='buscar')
    def buscar_por_id_ou_cnpj(self, request):
        id_empresa = request.query_params.get('id')
        cnpj = request.query_params.get('cnpj')
        
        empresa = None
        if id_empresa:
            empresa = Empresa.objects.filter(id=id_empresa).first()
        elif cnpj:
            empresa = Empresa.objects.filter(vCnpj=cnpj).first()
            
        
        if empresa:
            data = self.get_serializer(empresa).data
            data['endereco'] = EnderecoSerializers(empresa.iCod_endereco).data
            return Response(data)
        return Response({"detail": "Empresa não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    # V consultar por parte do nome fantasia
    @action(detail=False, methods=['get'], url_path='buscar-por-nome')
    def buscar_por_nome(self, request):
        nome = request.query_params.get('nome')
        
        if nome:
            empresa = Empresa.objects.filter(vNome_fantasia__icontains=nome)
            return Response(self.get_serializer(empresa, many=True).data)
        return Response({"detail": "Nome não fornecido"}, status=status.HTTP_400_BAD_REQUEST)