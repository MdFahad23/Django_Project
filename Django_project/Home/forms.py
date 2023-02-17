from django import forms
from django.core import validators
from Home.models import Musician, Album

# def even_or_not(args):
#     if args%2 == 1:
#         raise forms.ValidationError('Please Insert or Event Number!')
    

# class User_form(forms.Form):
    # User_name = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'placeholder':'Enter your full name.', 'style': 'width: 300px'}), validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(5)])

    # User_dob = forms.DateField(label='Date of Birth', widget=forms.TextInput(attrs={'type': 'date'}))

    # User_email = forms.EmailField(label='User Email', widget=forms.TextInput(attrs={'placeholder': 'Enter your email.'}))

    # field = forms.BooleanField(required=False)

    # field = forms.CharField(max_length=10, min_length=5)

    # choice = (('', '--Select Option--'), ('1', 'First'), ('2', 'Second'), ('3', 'Third'))
    # field = forms.ChoiceField(choices=choice, required=False )

    # choice = (('A', 'A'), ('B', 'B'), ('C', 'C'))
    # field = forms.ChoiceField(choices=choice, widget=forms.RadioSelect)

    # choice = (('', '--Select Option--'), ('1', 'First'), ('2', 'Second'), ('3', 'Third'))
    # field = forms.MultipleChoiceField(choices=choice, required=False )

    # choice = (('A', 'A'), ('B', 'B'), ('C', 'C'))
    # field = forms.MultipleChoiceField(choices=choice, widget=forms.CheckboxSelectMultiple)

    # field = forms.IntegerField(validators=[even_or_not])

    # user_email = forms.EmailField()
    # user_vEmail = forms.EmailField()

    # def clean(self):
    #     clean_data = super().clean()
    #     user_email = clean_data['user_email']
    #     user_vEmail = clean_data['user_vEmail']

    #     if user_email != user_vEmail:
    #         raise forms.ValidationError("Email Don't Match!!!")



class Musician(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
            


