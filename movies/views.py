from rest_framework.viewsets import ModelViewSet
from movies.serializers import MovieSerializer, ActorSerializer, GenreSerializer
from .models import Movie, Actor, Genres

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class=MovieSerializer

class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class=ActorSerializer

class GenreViewSet(ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class=GenreSerializer
    
