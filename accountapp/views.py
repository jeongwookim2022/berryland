from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm

# METHOD DECORATOR LIST
from articleapp.models import Article

has_ownership = [login_required, account_ownership_required]


# @login_required
# def hello(request):
#     # Authentication
#     if request.user.is_authenticated:
#         if request.method == "POST":
#
#             temp = request.POST.get('hello_input')
#
#             new_hello = Hello()
#             new_hello.text = temp
#             new_hello.save()
#
#             # hello_list = Hello.objects.all()
#
#             # ###After responding POST request, Redirect to current URL 'account/hello/'.###
#             # HttpResponseRedirect(reverse()) -> For not writing full URL.
#             # By doing so above, it's redirected the current URL.
#             # That means it's GET request then -> it renders 'hello.html' and sends 'hello_list'
#             # As a result, it shows every 'hello' in 'hello_list'.
#
#             # return render(request, 'accountapp/hello.html', context={'hello_list': hello_list})
#             return HttpResponseRedirect(reverse('accountapp:hello'))
#
#         else:
#             hello_list = Hello.objects.all()
#             return render(request, 'accountapp/hello.html', context={'hello_list': hello_list})

    # 1.
    # Not Authenticated
    # -> Redirect to Login page
    # else:
    #     return HttpResponseRedirect(reverse('accountapp:login'))

    # 2.
    # Used @login_required for the 2 lines of codes above.


# ################################## Class Based View ########################################
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello')  # It's CBV so using 'reverse()' throws an error.
    template_name = 'accountapp/create.html'


# 1. MultipleObjectMixin
# - To add 'Articles' in a specific 'Account'.
class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 3

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')
# -> Used A list of Decorators; 'has_ownership' to make it short.

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    # 1.
    # Customized UserCreationForm -> AccountUpdateForm
    # -> To prevent users from changing their IDs(Usernames).
    # form_class = UserCreationForm
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello')  # It's CBV so using 'reverse()' throws an error.
    template_name = 'accountapp/update.html'

    # 2.
    # Adjusted GET &POST methods to prevent UnAuthenticated user from viewing or updating his/her Info After logged out.
    # But he/she can still update/delete other people's info.
    # -> By using 'get_object()', can get 'User object' who is the current PK.
    #    And check if the current 'requesting user' is the same 'pk user'.

    # 3.
    # Too dirty. Should use Decorators but 'def get()' & 'def post()' are not FUNCTIONS but METHODS.
    # So, deleted them and used '@method_decorator()' for the class 'AccountUpdateView'.
    # '@method_decorator' makes 'decorators' that are used for normal FUNCTIONS become able to be used for 'METHODS'.
    #
    # 1) @method_decorator(login_required, 'get') & post
    # - This is for LOGIN only.
    #
    # 2) @method_decorator(account_ownership_required, 'get') & post
    # - This is for checking if the current 'requesting user' is
    #   the same 'pk user' who has the current PK.
    # 3) has_ownership
    # - A list that has decorators.
    # - This list will be inside of @method_decorator().

    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         # return HttpResponseRedirect(reverse('accountapp:login'))
    #         return HttpResponseForbidden()
    #
    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().post(*args, **kwargs)  # In decorator: return func(request, *args, **kwargs)
    #     else:
    #         # return HttpResponseRedirect(reverse('accountapp:login'))
    #         return HttpResponseForbidden()


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
