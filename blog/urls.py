from django.urls import path
from .views import *

urlpatterns = [
    path('', ListArticle.as_view(), name="home"),
    path('article/<int:id_article>', detail, name="detail"),
    path("article/recherche", search, name="search")
]
