from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import Hello


def hello(request):
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
    # Customized UserCreationForm -> AccountUpdateForm
    # -> To prevent users from changing their IDs.
    # form_class = UserCreationForm
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello')  # It's CBV so using 'reverse()' throws an error.
    template_name = 'accountapp/update.html'


class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
