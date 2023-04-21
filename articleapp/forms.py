from django import forms
from django.forms import ModelForm

from articleapp.models import Article


# 1. 'Writer' not in fields
# - Will set in server area. By using 'def form_valid(self)' in profileapp/views.py.

# 2. Added 'project' in fields
# 3. Added 'WYSIWIG'
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'height: auto;'}))

    # It allows users to not choose a project when creating an article.
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=True)

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']