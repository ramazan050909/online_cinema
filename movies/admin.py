from django.contrib import admin
from .models import Movie, Actor, Genres
from reviews.models import Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1  

class MovieAdmin(admin.ModelAdmin):
    inlines=[CommentInline]

class ActorAdmin(admin.ModelAdmin):
    readonly_fields=['image']

admin.site.register((Movie, Actor, Genres))
# Register your models here.
