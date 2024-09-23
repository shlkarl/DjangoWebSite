from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, "main.html")
def about (request):
    return render(request, "about.html")
def uslugi(request):
    return render(request, "uslugi.html") 
def direction(request):
    return render(request, "direction.html") 
def LK(request):
    return render(request, "LK.html") 
def server (request):
    return render(request, "server.html")
def product (request):
    return render(request, "product.html")
def service (request):
    return render(request, "service.html")
def its (request):
    return render(request, "its.html")
def base (request):
    return render(request, "its/base.html")
def prof (request):
    return render(request, "its/prof.html")
def contact (request):
    return render(request, "contact.html")

