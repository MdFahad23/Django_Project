from django import forms
from Home import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput({'type': 'date'}))
    class Meta:
        model = models.Album
        fields = '__all__'

