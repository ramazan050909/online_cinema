from rest_framework import serializers

from movies.models import Movie, Actor, Genres
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genres
        fields = '__all__'
        


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'




    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['actors'] = [actor.user.get_full_name() for actor in instance.actors.all()]

        return representation
    

