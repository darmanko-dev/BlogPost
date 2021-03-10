from django import forms
from django.forms import ModelForm
from .models import Post ,Comment



class PostForm(forms.Form):
    title = forms.CharField(label = "Le Title " , widget=forms.TextInput(
        attrs = {
            "class" : "form-control"
        }
    ))
    body = forms.CharField( label = "Le Body " , widget = forms.Textarea(
        attrs = {
            "class" : "form-control"
        }
    ))

    class Meta:
        model = Post
        fields = ['title','body']


class CommentForm(forms.ModelForm):
    user = forms.CharField( label = "User" , widget = forms.Select(
        attrs = {
            "class" : "form-control"
        }
    ))
    
    content = forms.CharField( label = "Content " , widget = forms.Textarea(
        attrs = {
            "class" : "form-control"
        }
    ))

    class Meta:
        model = Comment
        fields = ('user','content',)
