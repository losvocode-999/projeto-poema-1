
from django.contrib import admin
from django.urls import path
from . import views
from paginas.views import projeto_cordel
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
]
