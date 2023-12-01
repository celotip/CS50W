from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def serialize(self):
        return {
            "username": self.username,
            "id": self.id
        }

class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "likes": self.likes,
        }

class Follow(models.Model):
    follower = models.ForeignKey("User", on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey("User", on_delete=models.CASCADE, related_name="following")
    
    def serialize(self):
        return {
            "id": self.id,
            "follower": self.follower,
            "following": self.following,
        }

class Like(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="liker")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="liked")
    
    def serialize(self):
        return {
            "id": self.id,
            "liker": self.user,
            "liked": self.post,
        }

class Status(models.Model):
    status = models.BooleanField(default = False)
    def serialize(self):
        return {
            "status": self.status
        }