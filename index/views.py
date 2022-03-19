from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<h1>Cherry</h1>')

#def plantilla(request):
    #template = loader.get_template('plantilla.html')
    
    #plantilla_generada = template.render({})
    
    #return HttpResponse('plantilla_generada')
    
def plantilla(request):
    return render(request, 'index/plantilla.html')