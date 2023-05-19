from rest_framework import serializers
from .models import Movie, Review, Genre, Actor, Director

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Review
        fields = '__all__'
        
class DirectorSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Director
        fields = '__all__'
class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Genre
        fields = '__all__'
        
class ActorSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Actor
        fields = '__all__'