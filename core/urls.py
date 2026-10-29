from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/status/', views.status_api),
    path('api/status_nichos/', views.status_nichos_view, name='status_nichos'),
]
