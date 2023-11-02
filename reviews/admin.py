from django.contrib import admin

from .models import Rating, Comment, Favorite, Like



admin.site.register([Rating, Comment, Favorite, Like])