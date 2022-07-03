from django.shortcuts import render, redirect, get_object_or_404

from .forms import AlbumForm
from .models import Album


def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", {"albums": albums})


def new_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')   

    return render(request, "albums/new_album.html", {'form':form})   


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "albums/album_detail.html", {"album": album})


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else: 
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/edit_album.html", {"form": form, "album": album})                


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        return render(request, "albums/delete_album.html", {"album": album, "pk": pk})
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_album.html", {"album": album})        



