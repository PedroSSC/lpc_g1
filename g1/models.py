from django.db import models
from django.utils import timezone
# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField('nome', max_length = 200, unique = True)
    email = models.CharField('email',  max_length = 50)

class Evento(models.Model):
    nome = models.CharField('nome', max_length = 200)
    eventoPrincipal = models.CharField('evento principal', max_length = 200)
    sigla = models.CharField('sigla', max_length = 200)
    dataEHoradeInicio = models.DateField('data e hora inicio', default=timezone.now)
    palavrasChave = models.TextField('palavras chaves', blank=True, null=True)
    logotipo = models.TextField('logotipo', blank=True, null=True)
    realizador = models.ForeignKey('Pessoa', null=True)
    cidade = models.TextField('cidade', blank=True, null=True)
    uf = models.TextField('uf', blank=True, null=True)
    endereco = models.TextField('endereço', blank=True, null=True)
    cep = models.TextField('cep', blank=True, null=True)


    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()

        super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nome)

    class EventoCientifico(models.Model):
        issn = models.TextField('issn', blank=True, null=True)
        evento = models.ForeignKey('Evento', null=True)

    class ArtigoCientifico(models.Model):
        titulo = models.TextField('titulo', blank=True, null=True)
        eventoCientifico = models.ForeignKey('EventoCientifico', null=True)


    class ArtigoAutor(models.Model):
        ArtigoCientifico = models.ForeignKey('ArtigoCientifico', null=True)
        autor = models.ForeignKey('Pessoa', null=True)
