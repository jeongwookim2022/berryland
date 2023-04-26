from django.urls import path

from likeapp.views import LikeArticleView, DisLikeArticleView

app_name = 'likeapp'

urlpatterns = [
    path('article/like/<int:pk>', LikeArticleView.as_view(), name='article_like'),
    path('article/dislike/<int:pk>', DisLikeArticleView.as_view(), name='article_dislike'),

]