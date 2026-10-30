from django.contrib import admin
from django.urls import path, include
from core import views
from core.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path("", views.index, name="index"),
    path('', include('core.urls')),
]