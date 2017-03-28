from django.http import HttpResponse
from .models import Evento, Pessoa
# Create your views here.




def listaEventos(request):
    html = "<h1>Lista de Eventos</h1>"
    lista = Evento.objects.all()
    for evento in lista:
        html += '<li>{}</li>'.format(evento.nome)
    return HttpResponse(html)

def buscaEvento(request, id):
    evento = Evento.objects.get(pk = id)
    html = "<h1>Evento Encontrado:</h1>"
    html += '<li>{}</li>'.format(evento.nome)
    return HttpResponse(html)

def listaPessoas(request):
    html = "<h1>Lista de Pessoas</h1>"
    lista = Pessoa.objects.all()
    for pessoa in lista:
        html += '<li>{}</li>'.format(pessoa.nome)
    return HttpResponse(html)

def buscaPessoa(request, id):
    pessoa = Pessoa.objects.get(pk = id)
    html = "<h1>Pessoa Encontrada:</h1>"
    html += '<li>{}</li>'.format(pessoa.nome)
    return HttpResponse(html)
