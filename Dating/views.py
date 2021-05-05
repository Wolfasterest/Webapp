from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
     response = HttpResponse()
     response.writelines("<h1> Welcome to Test</h1>")
     response.write("Nooooooooooob")
     return response