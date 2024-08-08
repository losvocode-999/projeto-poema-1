from django.shortcuts import render
from.models import usuario

def login(request):
    return render(request,"todos/login.html")

def usuarios(request):
    novo_usuario = usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('senha')
    novo_usuario.save()

    return render(request,'usuario/usuarios.html',usuarios)

usuario = {
    'usuarios': usuario.objects.all()
}