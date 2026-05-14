from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def lista_veiculos(request):
    return render(request, 'veiculos/lista.html')

def detalhe(request):
    return render(request, 'veiculos/detalhe.html')