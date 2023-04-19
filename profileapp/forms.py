from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        # 1. fields
        # - Someone who is not you can make someone else's profile
        # - if 'user' is added in fields.
        # - So, notifying THE OWNER USER of Profile should be implemented
        # - in SERVER area not CLIENT area.
        # -> Used 'def form_valid(self, form)' in views.py
        fields = ['image', 'nickname', 'message']
