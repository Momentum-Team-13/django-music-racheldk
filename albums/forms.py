from django import forms
from .models import Album, Favorite

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'name', 
            'artist', 
        ]


class FavoriteForm(forms.ModelForm):
    class Meta:
        model=Favorite
        fields = [
            'user', 
            'album',
        ]
