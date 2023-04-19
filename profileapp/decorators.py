from django.http import HttpResponseForbidden
from profileapp.models import Profile


# 1.
# - Whatever Requests come, it will check if the pk belongs to a USER
#   that really sends the request. IF NOT, it will HttpResponseForbidden.


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated