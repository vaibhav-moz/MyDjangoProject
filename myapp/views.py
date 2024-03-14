from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    path = request.path
    return HttpResponse(path, content_type='text/html', charset='utf-8')

def users(request, name, id):
    return HttpResponse(f"Name: {name}, Id: {id}")

def getuser(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse(f"Name: {name}, ID: {id}")

def showform(request):
    return render(request, "form.html")