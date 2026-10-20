from django.http import JsonResponse


def status_api(request):
    """Informa ao armário se o servidor está online."""
    # O armário precisa saber se o servidor está acordado
    return JsonResponse({'status': 'online', 'sistema': 'Key Track IoT'})
