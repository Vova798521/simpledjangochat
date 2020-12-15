from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'myfirstapp/vovapage.html')

def lesyuck(request):
    return HttpResponse("<h4>клас </h4>")
