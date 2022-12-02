from django.http import HttpRequest

# Create your views here.

def index(request):
    return HttpRequest("Olá, mundo.Você está na página de votação.")
