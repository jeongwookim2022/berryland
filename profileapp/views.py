from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        # 1.
        # - Saving the data from 'ProfileCreationForm' Temporarily.
        #   So, it's not saved in DB by 'commit=False'.
        # - Still, there's no 'user' data yet.
        # - After Assigning the current 'REQUESTING USER's user' data
        #   into temp_profile.user, saved 'temp_profile'.
        # -> BASICALLY, Added user data to form data BECAUSE it doesn't
        #    have it before(no 'user' in FIELDS).

        temp_profile = form.save(commit=False)  # Temporarily here
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)
