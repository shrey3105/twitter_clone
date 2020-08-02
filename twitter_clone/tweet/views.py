from django.shortcuts import render
from tweet.models import Tweet,Comment
from tweet.forms import CreateTweet
from Users.models import Profile,Follow
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views.generic.detail import DetailView
# Create your views here.

def create_tweet(request):
    if request.method=='POST':
        message=request.POST['message']
        profile_obj=Profile.objects.get(user=request.user)
        t_obj=Tweet()
        t_obj.profile=profile_obj
        t_obj.message=message
        t_obj.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form=CreateTweet()
        return render(request,'tweet/create_tweet.html',{'form':form})


def comment_from_detail(request,pk):
    tweet_obj=Tweet.objects.get(pk=pk)
    profile_obj=Profile.objects.get(user=request.user)
    comment_obj=Comment()
    comment_obj.tweet=tweet_obj
    comment_obj.profile=profile_obj
    comment_obj.comment=request.POST['comment']
    comment_obj.save()
    return HttpResponseRedirect(reverse('tweet:comment_on_post',kwargs={'pk':pk}))

def recent_tweets(request):
    profile_obj=Profile.objects.get(user=request.user)
    arr=profile_obj.get_following_list()
    tweets=Tweet.objects.all().filter(profile__in=arr).order_by('-create_date')
    return render(request,'tweet/recent_tweets.html',{'tweets':tweets})

def like_tweet_from_feed(request,pk):
    obj=Tweet.objects.get(pk=pk)
    obj.likes=obj.likes+1
    obj.save()
    return recent_tweets(request)

def like_tweet(request,pk):
    obj=Tweet.objects.get(pk=pk)
    obj.likes=obj.likes+1
    obj.save()
    return HttpResponseRedirect(reverse('Users:profile',kwargs={'username':request.user.username}))

def delete_tweet(request,pk):
    obj=Tweet.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('Users:profile',kwargs={'username':request.user.username}))

class CommentOnPost(DetailView):
    template_name='tweet/comment_on_post.html'
    model=Tweet

def write_comment(request,pk):
    tweet_obj=Tweet.objects.get(pk=pk)
    profile_obj=Profile.objects.get(user=request.user)
    comment_obj=Comment()
    comment_obj.tweet=tweet_obj
    comment_obj.profile=profile_obj
    comment_obj.comment=request.POST['comment']
    comment_obj.save()
    return HttpResponseRedirect(reverse('Users:profile',kwargs={'username':request.user.username}))
