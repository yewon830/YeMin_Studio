from django.shortcuts import render, get_object_or_404
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
import json
# Create your views here.

# 회원가입
@api_view(['POST']) 
def sign_up(resquest):
    username = resquest.data.get('username')
    email = resquest.data.get('email')
    password1 = resquest.data.get('password1')
    password2 = resquest.data.get('password2')
    
    if password1 != password2:
        return Response({'error' : '비밀번호 확인에 실패하였습니다'}, status=400)
    
    try:
        user = User.objects.create_user(username=username, email=email, password=password1)
        refresh = RefreshToken.for_user(user)

        return Response({
            'success': '회원가입에 성공하였습니다',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
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
        refresh = RefreshToken.for_user(user)
        return Response({
            'success': '로그인에 성공하였습니다',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
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
    
    following_count = user.following.count()
    followers_count = user.followers.count()
    reviews = user.review_set.all()
    
    data = {
        'username': user.username,
        'profile_image': user.profile_image.url if user.profile_image else None,
        'following_count': following_count,
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
    
    user = request.user
    user.username = username
    user.profile_image = profile_image
    user.save()
    
    return Response({'success' : '프로필 수정에 성공하였습니다'})