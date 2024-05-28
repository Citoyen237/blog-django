from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .form import *
# Create your views here.
def login_blog(request):
    if request.method=="POST":
         form = LoginForm(request.POST)     
         if form.is_valid() :
              username = form.cleaned_data['username']
              pwd = form.cleaned_data['pwd']
              user=authenticate(username=username, password=pwd)
              if user is not None:
                   login(request, user)
                   return redirect('home')
              else :
                   messages.error(request, "Authentification echouer")
                   return render(request, 'connexion.html',{"form":form})
         else :
               for field in form.errors:
                    form[field].field.widget.attrs['class'] += ' is-invalid'
               return render(request, "connexion.html",{"form":form})
              
    else:
         form = LoginForm()  
         return render(request, "connexion.html",{"form":form})
    

def register(request):
         if request.method == 'POST':
              form = RegisterForm(request.POST)
              if form.is_valid():
                   username= username = form.cleaned_data['username']
                   pwd = form.cleaned_data['pwd']
               #     pwd_confirm =form.cleaned_data['pwd_confirm']
                   user = User.objects.create_user(username=username, password=pwd)
                   if user is not None :
                        return redirect('login')
                   else :
                        messages.error(request, ('Creation de compte echouee'))
                        return render(request, 'register.html',{'form':form})
              else:
                    return render(request, 'register.html',{'form':form})
              return render(request, 'register.html',{})
         form = RegisterForm()
         return render(request, 'register.html', {'form':form})
         
def logoutUser(request):
     logout(request)
     return redirect('home')
#     login=request.POST['login']
     #     '''Ancien connexion'''
#     pwd=request.POST['pwd']
     #     user=authenticate(username=login, password=pwd)
     #     if user is not None :
     #          return redirect("home")
     #     else:
     #          messages.error(request, "Erreur d'authentification")
     #          return render(request, "connexion.html")
#     return render(request, 'connexion.html')