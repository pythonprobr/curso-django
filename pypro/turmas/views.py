from django.shortcuts import render


def indice(request):
    return render(request, 'turmas/indice.html')
