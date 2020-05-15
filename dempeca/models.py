from django.db import models

# Create your models here.
class Peca(models.Model):
    idPeca = models.AutoField(primary_key=True)
    valor = models.FloatField()
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return '%d, %f, %s' % (self.idPeca, self.valor, self.descricao)
    def __repr_(self):
        return '%d, %f, %s' % (self.idPeca, self.valor, self.descricao)
    pass
   

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return '%d, %s' % (self.idUsuario, self.nome)
    def __repr__(self):
        return '%d, %s' % (self.idUsuario, self.nome)
    pass 

class Demanda(models.Model):
    idDemanda = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    status = models.IntegerField()

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pecas = models.ManyToManyField(Peca)

    def __str__(self):
        return '%d, %s, %s, %s, %s, %s, %s' % (self.idDemanda, self.rua, self.bairro, self.numero, self.cep, self.cidade, self.status)
    def __repr__(self):
        return '%d, %s, %s, %s, %s, %s, %s' % (self.idDemanda, self.rua, self.bairro, self.numero, self.cep, self.cidade, self.status)
    pass
