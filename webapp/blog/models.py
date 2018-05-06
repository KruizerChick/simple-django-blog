""" Models for Blog app """
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone

from taggit.managers import TaggableManager
from taggit.utils import parse_tags

User = get_user_model()

# Create your models here.
class PublishedManager(models.Manager):
    """ Manager model to return all published posts """
    def get_queryset(self):
        """ Published posts """
        return super(PublishedManager, self).get_queryset().filter(
            published_date__lte=timezone.now())


class Post(models.Model):
    """ Blog posts configuration """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()

    objects = models.Manager()
    published = PublishedManager()

    def publish(self):
        """ Sets published date to current time when published """
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        """ Filters comments by approved flag """
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        """ Sends user to detail page of post after making post """
        return reverse("blog:post_detail", kwargs={'pk':self.pk})

    # def get_tags(self):
    #     """ Returns parsed tag list """
    #     return self.tags.all|join:", "

    def __str__(self):
        return self.title


class Comment(models.Model):
    """ Blog post comments configuration """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        """ Sets approval flag to True """
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        """ Redirects commenter to list of posts after making comment """
        # return reverse("blog:post_detail")
        return reverse("blog:post_detail", kwargs={'pk':self.post_id})

    def __str__(self):
        return self.text
