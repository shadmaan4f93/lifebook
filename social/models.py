from django.db import models
from django.contrib.auth.models import User

class UserPost(models.Model):
    posted_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    posted_date = models.DateTimeField(auto_now_add=True)
    posted_update_date = models.DateTimeField(auto_now=True)
    user_post_description = models.TextField(blank=True)

class Comment(models.Model):
    post_id = models.IntegerField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.text

class Likes(models.Model):
    post_id = models.IntegerField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.CharField(max_length=50, default='like')
    like_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.likes
       

class News(models.Model):
    title = models.CharField(max_length=200)
    news_detail = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

class Event(models.Model):
    title = models.CharField(max_length=200)
    event_class = models.CharField(max_length=200, default='bg-blue')
    event_detail = models.TextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title 
