from django.urls import path,include
from . import views
app_name='tweet'

urlpatterns=[
path('create/',views.create_tweet,name='create_tweet'),
path('like_tweet_from_feed/<pk>/',views.like_tweet_from_feed,name='like_tweet_from_feed'),
path('like/<pk>/',views.like_tweet,name='like_tweet'),
path('comment_from_detail/<pk>/',views.comment_from_detail,name='comment_from_detail'),
path('delete/<pk>',views.delete_tweet,name='delete_tweet'),
path('comment_on_post/<pk>/',views.CommentOnPost.as_view(),name='comment_on_post'),
path('write_comment/<pk>/',views.write_comment,name='write_comment'),
path('recent_tweets/',views.recent_tweets,name='recent_tweets'),
]
