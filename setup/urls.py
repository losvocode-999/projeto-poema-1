
from django.contrib import admin
from django.urls import path

from todos.views import login
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login),
    path('usuarios/',views.usuarios,name="listagem_usuarios")
]
