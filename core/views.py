from django.http import JsonResponse
from django.shortcuts import render
from django.db import connection
from core.utils import dictfetchall


def status_api(request):
    """Informa ao armário se o servidor está online."""
    # O armário precisa saber se o servidor está acordado
    return JsonResponse({'status': 'online', 'sistema': 'Key Track IoT'})


def index(request):
    """Mostra a página inicial do Armário Inteligente de Chaves."""
    contexto = {'titulo': 'SENAI — Armário Inteligente de Chaves'}
    return render(request, 'index.html', contexto)


def status_nichos_view(request):
    """Devolve em JSON o status de todos os nichos lendo a view do banco."""
    try:
        # 1. Conexão e execução
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM vw_status_nicho;")

            # 2. Transformação
            dados_nichos = dictfetchall(cursor)
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "code": 500,
            "message": "Erro de conexão com o Supabase."
        }, status=500)

    return JsonResponse({
        "status": "success",
        "code": 200,
        "data": dados_nichos
    })
