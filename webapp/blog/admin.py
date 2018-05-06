""" Register Models for Blog app """
from django.contrib import admin

from .models import Post, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    """ Configure Admin appearance """
    list_display = ('title', 'id', 'author', 'published_date')
    list_filter = ('published_date', 'created_date', 'author')
    search_fields = ('title', 'text', 'tags')
    ordering = ['-published_date', '-created_date']

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    """ Configure Admin appearance """
    list_display = ('id', 'post', 'author', 'created_date', 'approved_comment')
    list_filter = ('approved_comment', 'created_date', 'author', 'post')
    search_fields = ('author', 'text')

admin.site.register(Comment, CommentAdmin)
