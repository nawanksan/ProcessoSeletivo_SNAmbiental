from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from endereco.api import viewsets as enderecoViewSet
from empresa.api import viewsets as empresaViewSet
from veiculo.api import viewsets as veiculoViewSet

router = routers.DefaultRouter()

router.register(r'endereco', enderecoViewSet.EnderecoViewSet, basename='enderecos')
router.register(r'empresa', empresaViewSet.EmpresaViewSet, basename='empresa')
router.register(r'veiculo', veiculoViewSet.VeiculoViewSet, basename='veiculo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
     path('', include(router.urls)),
]
