from django.urls import path
from . import views
app_name = 'movies'
urlpatterns = [
    path('', views.movie),  # 영화 추천 웹 페이지
    path('<int:movie_pk>/', views.movie_detail),  # 영화 상세 정보 팝업
    path('<int:movie_pk>/review/', views.movie_detail_review),  # 리뷰 팝업
    path('<int:movie_pk>/related/', views.movie_detail_related),  # 비슷한 영화 팝업
    path('page/<int:page_number>/', views.movie_page),  # 페이지 번호로 페이지로 이동
]