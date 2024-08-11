from django.shortcuts import render
from.models import usuario

def login(request):
    return render(request,"todos/login.html")

def usuarios(request):
    novo_usuario = usuario()
    novo_usuario.Nome = request.post.get('nome')
    novo_usuario.senha = request.post.get('senha')
    novo_usuario.save()

    return render(request,'todos/home.html',usuarios)

usuario = {
    'usuarios': usuario.objects.all()
}