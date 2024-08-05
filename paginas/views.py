from django.shortcuts import render

def pag_login(request):
    return render(request, 'pag_login/login.html')
