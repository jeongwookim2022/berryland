from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


# 1.
# - Whatever Requests come, it will check if the pk belongs to a USER
# - that really sends the request. IF NOT, it will HttpResponseForbidden.
def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated