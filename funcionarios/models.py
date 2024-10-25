from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=50, help_text='Insira o nome')
    cpf = models.CharField(max_length=11, help_text='Informe apenas numeros', unique=True)
    email = models.EmailField()
    data_cadastro = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True # Informando que essa classe é do tipo Abstrata

class Funcionario(Pessoa):
    cargo = models.CharField(max_length=20)
    meta = models.BigIntegerField()
    class Meta: #Informar os metadas da classe
        verbose_name = 'funcionario'
        verbose_name_plural = 'funcionarios'

    def __str__(self): # construtor da classe
        return self.cpf  #retorna o cpf no momento da criação do objeto.