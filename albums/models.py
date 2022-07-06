from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ManyToManyField("Artist", related_name="albums")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name

    def check_is_user_favorite(self, user):
        for favorite in self.favorites.all():
            if favorite.album == self: 
                return True 

    # related name on foreign key is the plural of the model it points to (the one that you're in). artist.albums will show all the albums that are related to that artist. 
    # ForeignKey is one to many. album can have 1 artist, artist can have many albums 


class Artist(models.Model):
    name = models.CharField(max_length=200)
    # could also add more info about artist, like genre or birthdate

    def __str__(self):
        return self.name


class User(AbstractUser):   
    pass   


class Favorite(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='favorites', null=True, blank=True)
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='favorites', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.album}'