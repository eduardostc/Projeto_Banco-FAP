from django.urls import path
from .views import FuncionarioAPIView

urlpatterns = [
    path('funcionarios/', FuncionarioAPIView.as_view(), name='funcionarios'),
]