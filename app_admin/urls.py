from django.urls import path
from .views import *

urlpatterns = [
    path('admin-blog/', index, name="home-admin"),
    path('mes-articles/',user_article, name='my-article'),
    path('ajouter-article/',AddArticle.as_view(), name='new-article'),
    path('update-article/<int:pk>',UpdateArticle.as_view(), name='update-article'),
    path('delete-article/<int:pk>',DeleteArticle.as_view(), name='delete-article'),
]
