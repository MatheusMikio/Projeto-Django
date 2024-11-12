from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import json
from . import getComentarioMLB


# def ver_produto(request):
#     return HttpResponse('Estou no ver')

def pesquisa_produto(request):
    if request.method == "GET":
        return render(request, 'index.html')
    
    elif request.method == "POST":
        #ignora 
        nome = request.POST.get('nome')
        listaprod = getComentarioMLB.getMLB(nome)
        img=getComentarioMLB.getMLBimg(nome)
        
        return render(request,'teladepesquisa.html',{'produto':listaprod,'img':img})

# def inserir_produto(request):
#     return HttpResponse('Estou no inserir')

# def escolher_produto():
# def visualizar_produto():
