""" Forms for Blog app """
from django import forms
from taggit.forms import TagWidget

from .models import Post, Comment

class PostForm(forms.ModelForm):
    """ Form to handle Blog Posts """
    class Meta:
        """ Form class info """
        model = Post
        fields = ('author', 'title', 'tags', 'text', )
        # Connect the form widgets to specific CSS styling
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(
                attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):
    """ Form to handle Comments on Blog Posts """
    class Meta:
        """ Form class info """
        model = Comment
        fields = ('author', 'text', )
        # Connect the form widgets to specific CSS styling
        widgets = {
            'author': forms.TextInput(
                attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(
                attrs={'class': 'editable medium-editor-textarea'}),
        }
