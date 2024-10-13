from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """Comment Form"""
    class Meta:
        model = Comment
        fields = ('body',)
