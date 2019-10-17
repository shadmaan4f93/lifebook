from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def get_upload_image_name(instance, filename):

    new_filename = str(instance.user.id) + ".jpg"
    return 'user/{0}'.format(new_filename)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=30, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    skils = models.CharField(max_length=30, blank=True)
    education = models.CharField(max_length=30, blank=True)
    edu_center = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    linkedin_profile = models.URLField(blank=True)
    twitter_profile = models.URLField(blank=True)
    facebook_profile = models.URLField(blank=True)
    image = models.ImageField(upload_to=get_upload_image_name , null=True, blank=True)

# class FriendsData(models.Model):
#     fromUserId = models.CharField(max_length=30, blank=True)
#     toUserId = models.CharField(max_length=30, blank=True)
#     status = models.BooleanField(default=False)
#     requestDate = models.DateTimeField(auto_now_add=True)
#     conformDate = models.DateTimeField(null=True, blank=True)
#     @classmethod
#     def addFriends(cls, current_user, new_friend):
#         print(current_user)
#         print(new_friend)
#         friendobj = FriendsData(fromUserId=current_user, toUserId=new_friend )
#         friendobj.save()
#     @classmethod
#     def removeFriends(cls, current_user, new_friend):
#         friend, created = cls.objects.get_or_create(
#             current_user=current_user
#         )
#         friend.users.add(new_friend)

class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.SET_NULL)
    status = models.BooleanField(default=False)
    requestDate = models.DateTimeField(auto_now_add=True)
    conformDate = models.DateTimeField(null=True, blank=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def conform_friend(cls, current_user, new_friend):
        f = Friend.objects.get(current_user=current_user)
        f.status = True
        f.save
    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)