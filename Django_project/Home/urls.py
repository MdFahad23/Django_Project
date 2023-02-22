from django.urls import path
from . import views

app_name = 'Home'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_musician/', views.musician_form, name='add_musician'),
    path('add_album/', views.album_form, name='add_album'),
    path('album_list/<int:artist_id>/', views.album_list, name='album_list'),
    path('edit_artist/<int:artist_id>/', views.edit_artist, name='edit_artist'),
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('delete_album/<int:delete_album_id>/', views.delete_album, name="delete_album"),
    path('delete_artist/<int:delete_artist_id>/', views.delete_artist, name='delete_artist')
]
