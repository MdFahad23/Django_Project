from django.shortcuts import render
from Home.models import Musician, Album
from Home import forms

# Create your views here.
def Home(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1': 'This is a Musician List', 'musician': musician_list}
    return render(request, 'Home/index.html', context=diction)

def Form(request):
    # new_form = forms.User_form()
    # diction = {'heading': "This is Create for Django Form.", 'new_form': new_form}
    new_form = forms.Musician()

    if request.method == 'POST':
        # new_form = forms.User_form(request.POST)
        # diction.update({'new_form': new_form})
        new_form = forms.Musician(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)

            # user_name = new_form.cleaned_data['User_name']
            # user_dob = new_form.cleaned_data['User_dob']
            # user_email = new_form.cleaned_data['User_email']
    
            # diction.update({'User_name': user_name})
            # diction.update({'User_dob': user_dob})
            # diction.update({'User_email': user_email})
            # diction.update({'field': new_form.cleaned_data['field']})
            # diction.update({'field': "SuccessFull!"})
            # diction.update({'Submitted': 'True'})

    diction = {'heading': "This is Create for Django Form.", 'new_form': new_form}    
    return render(request, "Home/Form.html", context=diction)
    