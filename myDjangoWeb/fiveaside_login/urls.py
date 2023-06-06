from django.contrib import admin
from django.urls import path

from myDjangoWeb.fiveaside_login import views

urlpatterns = [

    path('signup/',views.sign_up, name='signup'),
    path('login/',views.user_login, name='login'),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
]