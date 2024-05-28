from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    desc=models.TextField()
    image=models.ImageField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("mes-articles")
    