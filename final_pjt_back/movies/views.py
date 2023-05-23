from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Movie
from .serializers import MovieDetailSerializer, MovieSerializer
import json
import random
from functools import reduce
from operator import and_
# Create your views here.
@api_view(['GET'])
def movie_home(request, page_number):
    sort_option = request.GET.get('sort')  # 정렬 옵션을 요청에서 가져옴

    movie_list = list(Movie.objects.all())

    if sort_option == 'popularity':  # 인기순으로 정렬
        print('1')
        movie_list.sort(key=lambda movie: movie.popularity, reverse=True)
    elif sort_option == 'vote_average':  # 평점순으로 정렬
        print('2')
        movie_list.sort(key=lambda movie: movie.vote_average, reverse=True)
    elif sort_option == 'title':  # 가나다 순으로 정렬
        print('3')
        movie_list.sort(key=lambda movie: movie.title)

    paginator = Paginator(movie_list, 30)

    page_obj = paginator.get_page(page_number)
    movie_data = MovieSerializer(page_obj, many=True)

    # 현재 정렬 기준을 응답에 포함하여 전달
    response_data = {
        'movies': movie_data.data,
        'sort_option': sort_option
    }
    return Response(response_data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie  = get_object_or_404(Movie, pk = movie_pk)    
    movie_serializer = MovieDetailSerializer(movie)
    return Response(movie_serializer.data)

@api_view(['GET'])
def movie_search(request, sw_value):
    queries = [Q(title__icontains=char) for char in sw_value]
    movie_list = Movie.objects.filter(reduce(and_, queries))    
    
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

