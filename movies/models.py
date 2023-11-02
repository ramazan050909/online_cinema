from django.db import models
from django.utils.translation import gettext_lazy as _


class Actor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='actor/')
    birth_date = models.DateField(_('birth_date')) 
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Актёр'
        verbose_name_plural = 'Актёры'





class Genres(models.TextChoices):
    comedy = 'Комедия'
    horror = 'Хоррор'
    drama = 'Драма'
    thriller = 'Триллер'
    action = 'Боевик'
    documentary = 'Документальный'
    story = 'История'

class Genres(models.Model):
    genre = models.CharField(_('genre'),max_length=24, choices=Genres.choices)
    movies = models.ManyToManyField('Movie', blank=True)

    def __str__(self) -> str:
        return self.genre

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    title = models.CharField(_('title'),max_length=32)
    directors = models.CharField(max_length=120)
    genre = models.ManyToManyField('Genres')
    description = models.TextField(_('description'), blank=True)
    release = models.DateField()
    actors = models.ManyToManyField(Actor, related_name='movies')   

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

        

