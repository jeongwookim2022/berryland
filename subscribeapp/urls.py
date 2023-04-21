from django.urls import path

from subscribeapp.views import SubscribeView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
]