from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import json
from . import getComentarioMLB


# def ver_produto(request):
#     return HttpResponse('Estou no ver')

def ver_produto(request):
    if request.method == "GET":
        nome = 'Caio'
        return render(request, 'ver_produto.html', {'nome': nome})
    
    elif request.method == "POST":
        #ignora 
        nome = request.POST.get('nome')
        listaprod = getComentarioMLB.getMLB(nome)
        #ignora
        idade =request.POST.get('idade')
        
        return HttpResponse(listaprod)

# def inserir_produto(request):
#     return HttpResponse('Estou no inserir')

# def escolher_produto():
# def visualizar_produto():
