from django.db import models
from django.utils import timezone

# Create your models here.
class Album(models.Model):
    FAVORITE = 'Favorite'
    NOT_FAVORITE = 'Not a favorite'
    STATUS_CHOICES = [
        (FAVORITE, 'Favorite'),
        (NOT_FAVORITE, 'Not a favorite'),
    ]
    name = models.CharField(max_length=200)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE, related_name="albums",)
    created_at = models.DateTimeField(auto_now_add=True)
    favorite = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=NOT_FAVORITE,  
    )

    def __str__(self): 
        return self.name

    # related name on foreign key is the plural of the model it points to (the one that you're in). artist.albums will show all the albums that are related to that artist. 
    # ForeignKey is one to many. album can have 1 artist, artist can have many albums 


class Artist(models.Model):
    name = models.CharField(max_length=200)
    # could also add more info about artist, like genre or birthdate

    def __str__(self):
        return self.name


# class Favorite(models.Model):
#     status = models.CharField(max_length=20)

#     def __str__(self):
#         return self.status
