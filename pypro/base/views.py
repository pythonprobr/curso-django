from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('Olá Django')