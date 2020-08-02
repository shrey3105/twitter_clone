from django.db import models
from Users.models import Profile
from django.utils import timezone
# Create your models here.

class Tweet(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='tweets')
    message=models.TextField(max_length=100)
    create_date=models.DateTimeField(default=timezone.now())
    likes=models.IntegerField(default=0)

    def __str__(self):
        return self.message



class Comment(models.Model):
    tweet=models.ForeignKey(Tweet,on_delete=models.CASCADE,related_name='comments')
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    comment=models.TextField(max_length=100)
    likes=models.IntegerField(default=0)

    def __str__(self):
        return self.comment
