from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

def upload_to(instance, filename):
    return 'profile_pic/%s/%s' % (instance.user.username,filename)

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField(blank=True)
    profile_pic=models.ImageField(upload_to=upload_to,blank=True,default='profile_pic/None/no_image.jpg')

    def followers(self):
        return Follow.objects.filter(follows=self).count()
    def follower_count(self):
        return Follow.objects.filter(follows=self).count()

    def following(self):
        return Follow.objects.filter(user=self)

    def following_count(self):
        return Follow.objects.filter(user=self).count()

    def get_following_list(self):
        arr=[]
        follow_list=Follow.objects.all().filter(user=self)
        for obj in follow_list:
            arr.append(obj.follows)
        return arr 


    def __str__(self):
        return self.user.username


class Follow(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='source')
    follows=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='destination')
    follow_date=models.DateTimeField(default=timezone.now())

    def __str__(self):
        return "{} follows {}".format(self.user.user.username,self.follows.user.username)

    class Meta:
        unique_together=('user','follows')
