from unicodedata import name
from django.urls import path

from .import views

urlpatterns = [

    path('',views.userlogin, name='login'),
    path('signup',views.SignupPage,name='signup'),
    path('home',views.Homepage, name='home'),
    path('logout',views.LogoutPage,name='logout')
]