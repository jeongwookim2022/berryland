from django.forms import ModelForm

from articleapp.models import Article


# 1. 'Writer' not in fields
# - Will set in server area. By using 'def form_valid(self)' in profileapp/views.py.

# 2. Added 'project' in fields
class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']