from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_blog , name="login"),
    path('register/', register, name='register'),
    path('logout/', logoutUser, name='logout')
]