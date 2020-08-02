from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

app_name='Users'

urlpatterns=[
path('signup/',views.sign_up,name='signup'),
path('login/',auth_views.LoginView.as_view(template_name='Users/login.html'),name='login'),
path('logout/',auth_views.LogoutView.as_view(),name='logout'),
path('following/',views.show_following,name='show_following'),
path('followers/',views.show_followers,name='show_followers'),
path('follow_the_user/<username>/',views.add_to_follows,name='add_to_follows'),
path('profile/<username>/',views.profile,name='profile'),
path('new_connections/',views.new_connections,name='new_connections'),
]
