from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model =Article
        fiels = ['title','category','desc','image']
        exclude = ['created_at','updated_at','user']
        labels= {'title':'Titre','category':'Categorie','desc':'Description'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-select'}),
            'desc':forms.Textarea(attrs={'class':'form-control','row':4}),
        }