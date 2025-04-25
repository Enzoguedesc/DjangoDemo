from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo ao meu site! <br>"
    "Adicione o caminho /admin/ na URL para acessar o painel de administração. <br>"
    "Adicione o caminho /api/ na URL para acessar a API. <br>"
    "Adicione junto com /api/ o caminho /produtos/ para acessar os endpoints da API. <br>"
    "Adicione junto com /api/ o caminho /produtos/baratos/ para acessar os endpoints da API. <br>"
    "Adicione junto com /api/ o caminho /produtos/disponiveis/ para acessar os endpoints da API. <br>"
    "Adicione junto com /api/ o caminho /produtos/1/ para acessar os endpoints da API.")