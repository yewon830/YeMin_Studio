from django.shortcuts import render, get_object_or_404
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
import json
from movies.models import Movie
from movies.serializers import MovieDetailSerializer, MovieSerializer
from django.db.models import Count
from random import sample
import random
# Create your views here.

# 회원가입
@api_view(['POST']) 
def sign_up(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password1 = request.data.get('password1')
    password2 = request.data.get('password2')
    
    if password1 != password2:
        return Response({'error': '비밀번호 확인에 실패하였습니다'}, status=400)
    
    try:
        user = User.objects.create_user(username=username, email=email, password=password1)
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            'success': '회원가입에 성공하였습니다',
            'token': token.key,
        })
    except Exception as e:
        return Response({'error': str(e)}, status=400)

# 로그인
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            'success': '로그인에 성공하였습니다',
            'token': token.key,
        })
    else:
        return Response({'error': '다시 시도해주십시오'}, status=400)
    
# 로그아웃
@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'success': '로그아웃이 되었습니다'})

# 유저 프로필
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    
    followings_count = user.followings.count()
    followers_count = user.followers.count()
    reviews = user.reviews.all()
    
    data = {
        'username': user.username,
        'profile_image': user.profile_image.url if user.profile_image else None,
        'followings_count': followings_count,
        'followers_count': followers_count,
        'reviews': [review.text for review in reviews],
    }
    
    return Response(data)

# 회원 정보 수정
@api_view(['POST'])
@login_required
def profile_update(request):
    username = request.data.get('username')
    profile_image = request.data.get('profile_image')
    password = request.data.get('password')
    
    user = request.user
    user.username = username
    user.profile_image = profile_image
    user.password = password
    user.save()
    
    return Response({'success' : '프로필 수정에 성공하였습니다'})

# 내 컨텐츠
@api_view(['GET'])
@login_required
def mycontents(request):
    user = request.user
    
    # user의 like_movie 데이터 가져오기
    like_movie_data = Movie.objects.filter(like_users=user)
    
    # user의 wishlist_movie 데이터 가져오기
    wishlist_movie_data = Movie.objects.filter(wishlist=user)
    
    # 좋아요한 영화 데이터
    like_movies = list(like_movie_data.values())
    
    # 위시리스트 영화 데이터
    wish_movies = list(wishlist_movie_data.values())
    
    # Response를 사용하여 데이터 반환
    return Response({
        'like_movies': like_movies,
        'wish_movies': wish_movies
    })

# 팔로우 팔로잉
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    person = get_object_or_404(User, pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return Response(status=204)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def commend_movies(request):
    user = request.user
    
    liked_movies = user.likes.all().values_list('movie', flat=True)
    liked_genres = Movie.objects.filter(id__in=liked_movies).values_list('genre', flat=True)
    genre_counts = Movie.objects.exclude(id__in=liked_movies).exclude(genre__isnull=True).values('genre').annotate(count=Count('genre')).order_by('-count')

    if genre_counts.exists():
        top_genre = genre_counts[0]['genre']
        movies = Movie.objects.filter(genre=top_genre).exclude(id__in=liked_movies).order_by('-likes')

        if movies.count() < 5:
            next_genre_movies = Movie.objects.filter(genre__in=liked_genres).exclude(id__in=liked_movies).order_by('-likes')
            movies = movies.union(next_genre_movies)[:5]
            
        movies = random.sample(list(movies), min(5, movies.count()))

        movie_list = []
        for movie in movies:
            movie_data = MovieSerializer(movie).data
            movie_list.append(movie_data)

        data = {
            'movies': movie_list
        }
    else:
        data = {
            'movies': []
        }
    return Response(data)