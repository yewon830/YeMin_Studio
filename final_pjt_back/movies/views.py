from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Review
from .serializers import MovieDetailSerializer, MovieSerializer, ReviewSerializer
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
        liked = False
    else:
        movie.like_users.add(request.user)
        liked = True
    
    return Response({'liked': liked})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def wish(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if movie.wishlist.filter(pk=request.user.pk).exists():
        movie.wishlist.remove(request.user)
        wished = False
    else:
        movie.wishlist.add(request.user)
        wished = True
    
    return Response({'wished': wished})

# 리뷰 리스트
@api_view(['GET'])
def get_review_list(request, movie_id):
    reviews = Review.objects.filter(movie_id=movie_id)
    serialized_reviews = ReviewSerializer(reviews, many=True)
    return Response(serialized_reviews.data)


# 리뷰 작성
@api_view(['POST'])
def create_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# 리뷰 수정, 삭제
@api_view(['PUT', 'DELETE'])
def update_or_delete_review(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(status=404)

    # 작성자 본인만 수정 및 삭제 가능
    if review.user != request.user:
        return Response(status=403)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=204)