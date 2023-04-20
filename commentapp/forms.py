from django.forms import ModelForm

from commentapp.models import Comment


# 1.fields
# - The value that needs to be typed by input is 'content' only.
class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']