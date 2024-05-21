from django.urls import path
from app.views import *

urlpatterns = [
     path('',register,name='register'),
     path('login',login,name='login'),
     path('logout',logout,name='logout'),
     path('edit_profile',edit_profile,name='edit_profile'),
     path('change_password',change_password,name='change_password'),
     path('view_profile', view_profile, name='view_profile'),
     path('base',base, name='base'),
     
]