from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='+', null=True)
    following = models.ForeignKey(User,  related_name='+', null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_follower(self):
        return self.follower

    def get_following(self):
        return self.following

class Tag(models.Model):
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Photo(models.Model):
    owner = models.ForeignKey(User, null=True)
    caption = models.TextField(max_length=255)
    image = models.ImageField(upload_to="uploads/photos", null=True)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption

class Like(models.Model):
    owner = models.ForeignKey(User, null=True)
    photo = models.ForeignKey(Photo, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.photo

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/dp", null=True)
