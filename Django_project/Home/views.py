from django.shortcuts import render
from Home.models import Musician, Album
from Home import forms
from django.db.models import Avg

# Create your views here.
def index(request):
    musician_list  = Musician.objects.all()
    diction = {'title': 'Home Page', 'musician_list': musician_list}
    return render(request, 'Home/index.html', context=diction)

def album_list(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_info = Album.objects.filter(artist=artist_id)
    album_rating = Album.objects.filter(artist=artist_id).aggregate(Avg("num_start"))
    diction = {'title': 'List of Album', 'artist_info': artist_info, 'album_info': album_info, 'album_rating': album_rating}
    return render(request, 'Home/album_list.html', context=diction)

def musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)

        if form.is_valid:
            form.save(commit=True)
            return index(request)

    diction = {'title': 'Add Musician', 'musician_form': form}
    return render(request, 'Home/musician_form.html', context=diction)

def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)

        if form.is_valid:
            form.save(commit=True)
            return index(request)

    diction = {'title': 'Add Album', 'album_form': form}
    return render(request, 'Home/album_form.html', context=diction)

def edit_artist(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)

    if request.method == "POST":
        form = forms.MusicianForm(request.POST, instance=artist_info)

        if form.is_valid:
            form.save(commit=True)
            return album_list(request, artist_id)

    diction = {'edit_form':form}
    return render(request, 'Home/edit_musician.html', context=diction)

def edit_album(request, album_id):
    diction = {}

    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)

    if request.method == "POST":
        form = forms.AlbumForm(request.POST, instance=album_info)

        if form.is_valid:
            form.save(commit=True)
            diction.update({'success': 'Successfully Update!'})

    diction.update({'album_form': form})
    return render(request, 'Home/edit_album.html', context=diction)


def delete_album(request, delete_album_id):
    album = Album.objects.get(pk=delete_album_id).delete()
    
    diction = {'delete_success': "Successfully Delete Album!"}
    return render(request, "Home/delete.html", context=diction)

def delete_artist(request, delete_artist_id):
    artist = Musician.objects.get(pk=delete_artist_id).delete()
    diction = {'delete_success': "Successfully Delete Artist!"}
    return render(request, "Home/delete.html", context=diction)
