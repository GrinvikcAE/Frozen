from django.db import models
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey

from ..comments.models import AbstractComment


class Post(models.Model):
    """Post model"""
    text = models.TextField(max_length=512)
    created_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    moderation = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'id {self.id}'

    def comments_count(self):
        return self.comments.count()


class Comment(AbstractComment, MPTTModel):
    """Model of comments to posts"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    def __str__(self):
        return f'{self.user} - {self.post}'
