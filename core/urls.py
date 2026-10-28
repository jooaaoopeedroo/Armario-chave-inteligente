from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/status/', views.status_api, name='status_api'),
    path('api/status_nichos/', views.status_nichos_view, name='status_nichos'),
]
