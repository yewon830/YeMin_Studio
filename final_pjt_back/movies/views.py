from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Movie
from .serializers import MovieDetailSerializer, MovieSerializer
import json
import random

# Create your views here.
@api_view(['GET'])
def movie_home(request):
    movie_list = list(Movie.objects.all())
    random.shuffle(movie_list)
    paginator = Paginator(movie_list, 30)
    
    page_number = 1
    page_obj = paginator.get_page(page_number)
    movie_data = MovieSerializer(page_obj, many=True)
    return Response(movie_data.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie  = get_object_or_404(Movie, pk = movie_pk)    
    movie_serializer = MovieDetailSerializer(movie)
    return Response(movie_serializer.data)

@api_view(['GET'])
def movie_search(request, sw_value):
    movie_list = Movie.objects.filter(Q(title__contains=sw_value) | Q(overview__contains=sw_value))
    
    paginator = Paginator(movie_list, 30)
    
    page_number = 1
    page_obj = paginator.get_page(page_number)
    movie_data = MovieSerializer(page_obj, many=True)
    return Response(movie_data.data)

# def movies(request, page):
#     movie_list = []
#     for i in range(1001):
#         movie_list.append(f'movie{i}')
#     start = (page - 1) * 30
#     end = start + 30
#     movies = movie_list[start:end]
#     return JsonResponse(movies, safe=False)    