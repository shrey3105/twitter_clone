from django.shortcuts import render
from django.contrib.auth.models import User
from Users.forms import ProfileForm
from Users.models import Profile,Follow
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request,'index.html')

def profile(request,**kwargs):
    name=kwargs['username']
    user=User.objects.get(username=name)
    profile_obj=Profile.objects.get(user=user)
    path=profile_obj.profile_pic.url
    follower_count=profile_obj.follower_count()
    following_count=profile_obj.following_count()
    return render(request,'Users/profile.html',{'profile':profile_obj,'path':path,'follower':follower_count,'following':following_count})

def show_followers(request):
    profile_obj=Profile.objects.get(user=request.user)
    follow_obj=Follow.objects.all().filter(follows=profile_obj).order_by('-follow_date')
    return render(request,'Users/show_followers.html',{'follower_obj':follow_obj})

def show_following(request):
    profile_obj=Profile.objects.get(user=request.user)
    following_obj=Follow.objects.all().filter(user = profile_obj).order_by('-follow_date')
    return render(request,'Users/show_following.html',{'following_obj':following_obj})

def new_connections(request):
    profile_obj=Profile.objects.get(user=request.user)
    arr=profile_obj.get_following_list()
    all_profiles=Profile.objects.all()
    new_list=[]
    for obj in all_profiles:
        if obj not in arr:
            new_list.append(obj)
    return render(request,'Users/new_connections.html',{'profiles':new_list})

def add_to_follows(request,**kwargs):
    user1=request.user
    user2=User.objects.get(username=kwargs['username'])
    p1=Profile.objects.get(user=user1)
    p2=Profile.objects.get(user=user2)
    follow_obj=Follow()
    follow_obj.user=p1
    follow_obj.follows=p2
    follow_obj.save()
    return HttpResponseRedirect(reverse('Users:new_connections'))


def sign_up(request):
    if request.method=="POST":
        form=ProfileForm(request.POST,request.FILES)
        username=request.POST['username']
        password=request.POST['password']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        description=request.POST['description']
        user=User()
        user.username=username
        user.first_name=first_name
        user.last_name=last_name
        user.set_password(password)
        user.save()
        profile_obj=Profile()
        profile_obj.user=user
        if description:
            profile_obj.description=description
        if request.FILES.get('profile_pic'):
            profile_obj.profile_pic=request.FILES.get("profile_pic")
        profile_obj.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form=ProfileForm()
        return render(request,'Users/signup.html',{'form':form})
