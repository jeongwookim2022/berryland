from django.urls import path

from accountapp.views import hello

app_name = "accountapp" ### "127.0.0.1:8000/account/hello" -> "accountapp:hello"


urlpatterns = [
    path('hello/', hello, name="hello")

]