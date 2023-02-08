from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Blog(request):
    return render(request, 'Blog\index.html')

