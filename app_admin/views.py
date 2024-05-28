from typing import Any
from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from blog.models import Article
from blog.form import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView




# Create your views here.
def index(request):
   return render(request, 'dashboard.html')

@login_required
def user_article(request):
   has_perm = False
   if request.user.has_perm("blog.delete_article"):
      has_perm = True
   # if not request.user.is_authenticated:
   #    return redirect('login')
   # else: 
   listesArticles = Article.objects.filter(user=request.user)
   return render(request, 'my-article.html',{'listes':listesArticles,'has_perm':has_perm})
   
class AddArticle(LoginRequiredMixin,CreateView):
   model = Article
   form_class=ArticleForm
   template_name="add-article.html"
   success_url="../mes-articles"


   def form_valid(self, form):
       form.instance.user=self.request.user
       return super().form_valid(form)
   
class UpdateArticle(LoginRequiredMixin,UpdateView):
   model = Article
   form_class=ArticleForm
   template_name="article-form.html"
   success_url="../mes-articles"

class DeleteArticle(LoginRequiredMixin,DeleteView):
   model=Article
   success_url="../mes-articles"
   template_name="delete-article.html"
   success_url="../mes-articles"

   # def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
   #    return super().dispatch(request, *args, **kwargs)

'''Vue fonder sur les classes'''
'''queries'''
'''django template format'''