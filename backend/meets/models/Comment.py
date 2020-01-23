from django.db import models
from django.contrib.auth.models import User
from .Meet import Meet


class Comment(models.Model):
    post = models.ForeignKey(Meet, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=True, null=True)

    # TODO create a custom method to fill username
    @property
    def save_username(self):
        self.username = User.username
        self.save()

    def __str__(self):
        return self.comment[:20]
