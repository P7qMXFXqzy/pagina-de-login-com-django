from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from app.models import Usuarios

def carregarPagina(request):
    template = loader.get_template('index.html')
    dados = Usuarios.objects.all().values().order_by('nomeUsuario') 
    grupo = {"dados":dados}
    print(grupo)
    return HttpResponse(template.render(grupo))

def paginaConectado(request):
    template = loader.get_template('paginaConectado.html')
    return HttpResponse(template.render())

def retornarDados(request):
    dados_f = Usuarios.objects.all().values.order_by('nomeUsuario') 
    """
    dados_f_html = []
    for instance in Usuarios.objects.all():  # it's not serialization, but extracting of the useful fields
        dados_f_html.append({'pk': instance.pk, 'title': instance.nomeUsuario, 'body': instance.senha})
    dados_dic = {'dados_f': dados_f, 'ac_tab_n': 'ac_tab', 'dados_f_html': dados_f_html}
    """
    print(dados_f)
    return render(request, 'index.html', dados_f)
