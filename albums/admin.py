from django.contrib import admin
from .models import Album, Artist, Favorite

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Favorite)
