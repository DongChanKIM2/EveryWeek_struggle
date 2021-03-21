from django.contrib import admin
from . import models
# from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'overview', 'poster_path' ]
    list_display_links = ['id', 'title']

admin.site.register(models.Movie, MovieAdmin)