from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Blog(request):
    return HttpResponse('<h1>This is Blog Page</h1>')
