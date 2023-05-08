from unicodedata import name
from django.urls import path

from .import views

urlpatterns = [
    path('adminlogin',views.adminlogin, name='adminlogin'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('adminsearch',views.search,name='adminsearch'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('admindelete <int:id>',views.admindelete,name='admindelete'),
    path('userupdate <int:id>',views.userupdate,name='userupdate'),
    path('doupdate <int:id>',views.doupdate,name='doupdate'),
    path('adduser',views.adduser,name='adduser'),
    
  
]
