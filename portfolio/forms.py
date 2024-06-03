from django import forms
from .models import *

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-comment-name'}),
            'body': forms.Textarea(attrs={'class': 'form-comment-body'}),
        }


class AddReply(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('name', 'reply')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-comment-name'}),
            'reply': forms.Textarea(attrs={'class': 'form-comment-body'}),
        }