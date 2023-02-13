from django.shortcuts import render
from Home.models import Musician, Album

# Create your views here.
def Home(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1': 'This is a Musician List', 'musician': musician_list}
    return render(request, 'Home/index.html', context=diction)
