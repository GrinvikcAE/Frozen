from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from mptt.admin import MPTTModelAdmin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Comments to posts"""
    list_display = ('user', 'text', 'moderation', 'created_date', 'published', 'view_count', 'id')


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """Comments to posts"""
    list_display = ('user', 'text', 'post', 'created_date', 'update_date', 'published', 'id')
    mppt_level_indent = 15
