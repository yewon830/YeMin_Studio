from django.urls import path
from . import views
app_name = 'movies'
urlpatterns = [
    path('', views.movie_home),  # 영화 추천 웹 페이지
    path('d=<int:movie_pk>/', views.movie_detail),  # 영화 상세 정보 팝업
    path('<str:sw_value>/', views.movie_search), # 검색어에 따른 페이지
    # path('page/<int:page_number>/', views.movie_page),  # 페이지 번호로 페이지로 이동
]