from django.urls import path
from .views import FuncionarioAPIView, FuncionariosAPIView, CreateFuncionarioAPIView

urlpatterns = [
    path('funcionario/<int:pk>', FuncionarioAPIView.as_view(), name='funcionario'),
    path('funcionarios/', FuncionariosAPIView.as_view(), name='funcionarios'),
    path('create/', CreateFuncionarioAPIView.as_view(), name='create'),

]