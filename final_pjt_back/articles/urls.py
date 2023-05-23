from django.urls import path, include
from . import views
app_name = 'articles'

urlpatterns = [
    path('' , views.article_list),
    path('<int:article_pk>/' , views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('<int:article_pk>/comments/', views.comment_create),
]
