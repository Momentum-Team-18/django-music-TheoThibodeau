from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'album_title', 'song_list', 'published_date', 'image')