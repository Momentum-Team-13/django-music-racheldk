from django.shortcuts import render, redirect, get_object_or_404

from .forms import AlbumForm, FavoriteForm
from .models import Album, Artist, Favorite


def list_albums(request):
    albums = Album.objects.all()
    favorite_albums = [album for album in albums if album.check_is_user_favorite(request.user)]
        
    return render(request, "albums/list_albums.html", {"albums": albums, "favorite_albums": favorite_albums})


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


def list_by_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'albums/list_by_artist.html', {"artist": artist})
    

def add_favorite(request, pk):
    album = get_object_or_404(Album, pk=pk)
    favorite = Favorite.objects.create(album=album, user=request.user)
    favorite.save()
    return redirect(to="list_albums")

    # if request.method == "GET":
    #     form = FavoriteForm
    # else: 
    #     form = FavoriteForm(data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect(to='list_albums')
    # return render(request, "albums/add_favorite.html", {"form": form, "album": album})      


def delete_favorite(request, pk):
    album = get_object_or_404(Album, pk=pk)
    favorite = album.favorites.get(user=request.user)
    if request.method == 'GET':
        return render(request, "albums/delete_favorite.html", {"album": album, "pk": pk})
    if request.method == 'POST':
        favorite.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_favorite.html", {"album": album})   