from django.db import models


class AbstractComment(models.Model):
    """Abstract comment model"""
    text = models.TextField(max_length=512)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    moderation = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        abstract = True

