from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlbumForm
from .models import Album
from .forms import ArtistForm
from .models import Artist

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music_app/index.html', {'albums': albums})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'music_app/artist_list.html', {'artists': artists})

def new_artist(request):
    artists = Artist.objects.all()
    return render(request, 'music_app/new_artist.html', {'artists': artists})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'music_app/album_detail.html', {'album': album})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'music_app/artist_detail.html', {'artist': artist})

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('home')

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    
    if request.method == 'GET':
        form = AlbumForm(instance=album)
        # passing the instance argument puts the existing
        # data in the form
    else:
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'music_app/edit_album.html', {'form': form})

def create_album(request):
    # create new album
    if request.method == 'GET':
        form = AlbumForm()
        # if the user visits the page, render a blank form
    else:
        # django forms only handle GET and POST, so submitting the form will be a POST request
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Saves an instance of a new album in the database
            return redirect('home')
    return render(request, 'music_app/new_album.html', {'form': form})

def create_artist(request):
    if request.method == 'GET':
        form = ArtistForm()
    else:
        form = ArtistForm(request.POST, request)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'music_app/new_artist.html', {'form': form})

def albums_by_label(request, label_pk):
    label = get_object_or_404(Label, pk=Label)
    album = Album.objects.filter(label_id=label_pk)
    context = {
        'label': label,
        'albums': album,
    }
    return render(request, 'albums/albums_by_pub.html', context)
