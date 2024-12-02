"""
URL configuration for Escuela project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Gestion.views import buscar_todos, registro_personas, enviar_correo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buscar-todos/', buscar_todos, name='buscar_todos'),
    path('registro-personas/', registro_personas, name='registro_personas'),
    path('enviar-correo/', enviar_correo, name='enviar_correo'),
]
