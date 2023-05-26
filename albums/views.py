from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlbumForm
from .models import Album

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music_app/index.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'music_app/album_detail.html', {'album': album})

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('home')

def cover(request, pk):
    albums = Album.objects.all()
    return render(request, 'music_app/album_detail.html', {'albums': albums})

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
        form = AlbumForm(request.POST)
        form.save()
        # Saves an instance of a new album in the database
        return redirect('home')
    return render(request, 'music_app/new_album.html', {'form': form})

def albums_by_label(request, label_pk):
    label = get_object_or_404(Label, pk=Label)
    album = Album.objects.filter(label_id=label_pk)
    context = {
        'label': label,
        'albums': album,
    }
    return render(request, 'albums/albums_by_pub.html', context)
