from django import forms
from .models import Album
from .models import Artist

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'album_title', 'song_list', 'published_date', 'image')

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'album_list')