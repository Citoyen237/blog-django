from django.shortcuts import render
from .models import Article
from django.views.generic import ListView

def home(request):
    articles = Article.objects.all()
    context={"articles":articles}
    return render(request,"home.html", context)
# Create your views here.

def detail(request, id_article):
    article=Article.objects.get(id=id_article)
    category=article.category
    article_category=Article.objects.filter(category=category)
    return render(request,'detail.html',{"article":article,"categorys":article_category})

def search(request):
    query=request.GET['article']
    liste_article=Article.objects.filter(title__icontains=query)
    context={"liste_articles":liste_article}
    return render(request, 'search.html', context)


class ListArticle(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 10
    model = Article
    template_name = "home.html"
