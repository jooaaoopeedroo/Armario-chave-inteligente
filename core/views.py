from django.http import JsonResponse
from django.shortcuts import render


def status_api(request):
    """Informa ao armário se o servidor está online."""
    # O armário precisa saber se o servidor está acordado
    return JsonResponse({'status': 'online', 'sistema': 'Key Track IoT'})


def index(request):
    """Mostra a página inicial do Armário Inteligente de Chaves."""
    contexto = {'titulo': 'SENAI — Armário Inteligente de Chaves'}
    return render(request, 'index.html', contexto)
