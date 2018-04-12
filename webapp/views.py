from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Página de bienvenida de kiddysBigMoments")
