from django.urls import path

from subscribeapp.views import SubscribeView, SubscribeListView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('list/', SubscribeListView.as_view(), name='list'),

]