from django.urls import path

from pypro.modulos import views

app_name = 'modulos'
urlpatterns = [
    path('form', views.form, name='form'),
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('aulas/<slug:slug>', views.aula, name='aula'),
    path('api/aulas/<slug:slug>', views.aula_api, name='aula_api'),
    path('', views.indice, name='indice'),

]
