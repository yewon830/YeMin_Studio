from django.urls import path, include
from . import views
from dj_rest_auth.registration.views import RegisterView
app_name = 'accounts'

urlpatterns = [
    # path('users')
    path('', include('dj_rest_auth.urls')),
    path('signup/', views.sign_up, name='sign-up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile-update'),
    # path('userinfo/', views.userinfo),
    # path('userinfo/', views.userinfo),
    # path('userinfo/', views.userinfo),
]
