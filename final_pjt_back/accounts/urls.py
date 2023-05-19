from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('users')
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    # path('userinfo/', views.userinfo),
    # path('userinfo/', views.userinfo),
    # path('userinfo/', views.userinfo),
    # path('userinfo/', views.userinfo),
]
