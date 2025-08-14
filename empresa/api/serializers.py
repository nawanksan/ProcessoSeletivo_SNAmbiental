from rest_framework import serializers
from empresa.models import Empresa

class EmpresaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'