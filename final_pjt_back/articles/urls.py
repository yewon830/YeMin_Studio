from django.urls import path, include
from . import views
app_name = 'articles'

urlpatterns = [
    path('' , views.article_list),
    path('<int:article_pk/' , views.article_detail),
]
