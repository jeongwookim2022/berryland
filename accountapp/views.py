from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import Hello


def hello(request):
    # Authentication
    if request.user.is_authenticated:
        if request.method == "POST":

            temp = request.POST.get('hello_input')

            new_hello = Hello()
            new_hello.text = temp
            new_hello.save()

            # hello_list = Hello.objects.all()

            # ###After responding POST request, Redirect to current URL 'account/hello/'.###
            # HttpResponseRedirect(reverse()) -> For not writing full URL.
            # By doing so above, it's redirected the current URL.
            # That means it's GET request then -> it renders 'hello.html' and sends 'hello_list'
            # As a result, it shows every 'hello' in 'hello_list'.

            # return render(request, 'accountapp/hello.html', context={'hello_list': hello_list})
            return HttpResponseRedirect(reverse('accountapp:hello'))

        else:
            hello_list = Hello.objects.all()
            return render(request, 'accountapp/hello.html', context={'hello_list': hello_list})

    # Not Authenticated
    # -> Redirect to Login page
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))


# ################################## Class Based View ########################################
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello')  # It's CBV so using 'reverse()' throws an error.
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    # Customized UserCreationForm -> AccountUpdateForm
    # -> To prevent users from changing their IDs.
    # form_class = UserCreationForm
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello')  # It's CBV so using 'reverse()' throws an error.
    template_name = 'accountapp/update.html'

    # Adjusted GET &POST methods to prevent UnAuthenticated user from viewing or updating his/her Info After logged out.
    # But he/she can still update/delete other people's info.
    # -> By using 'get_object()', can get 'User object' who is the current PK.
    #    And check if the current 'requesting user' is the same 'pk user'.
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            # return HttpResponseRedirect(reverse('accountapp:login'))
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            # return HttpResponseRedirect(reverse('accountapp:login'))
            return HttpResponseForbidden()


class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()