from django.shortcuts import render

# Create your views here.
def Home(request):
    dictatory = {'text_1': 'Home Page is Defined!'}
    return render(request, 'Home/index.html', context=dictatory)
