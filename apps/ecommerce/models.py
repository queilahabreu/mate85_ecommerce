from django.db import models

# Create your models here.
class Administrador(models.Model):
    
    nome = models.CharField(max_length=50)
    foto = models.ImageField()

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    
    nome = models.CharField(max_length=50)
    cep_endereco = models.CharField(max_length=10,verbose_name="CEP")
    estado_endereco = models.CharField(max_length=4,verbose_name="Estado") 
    cidade_endereco = models.CharField(max_length=30,verbose_name="Cidade")
    bairro_endereco = models.CharField(max_length=30,verbose_name="Bairro")
    endereco_endereco = models.CharField(max_length=200,verbose_name="Endereço")
    numero_endereco = models.CharField(max_length=10,verbose_name="Número Endereço")

class Produto(models.Model):
    
    nome = models.CharField(max_length=100)
    imagem = models.ImageField()
    data_de_registro = models.DateField(auto_now_add=True)
    registrador = models.ForeignKey(Administrador, on_delete=models.PROTECT)