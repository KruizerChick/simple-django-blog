""" Template Tags for Blog app """
from django import template
from django.db.models import Count
# from django.utils.safestring import mark_safe
# import markdown

# from taggit.models import Tag, TaggedItem

from ..models import Post, Comment

register = template.Library()

@register.simple_tag
def total_posts():
    """ Returns the total number of posts """
    return Post.published.count()


@register.simple_tag
def total_draft_posts():
    """ Returns the total number of draft posts """
    total = Post.objects.count()
    pub = Post.published.count()
    return total - pub


@register.inclusion_tag('blog/_latest_posts.html')
def show_latest_posts(count=5):
    """ Display the most recent published posts, default of 5 posts """
    latest_posts = Post.published.order_by('-published_date')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def show_popular_posts(count=5):
    """ Displays the posts with the most comments,
    excluding those with no comments """
    return Post.published.annotate(
        total_comments=Count('comments')).exclude(
            total_comments__lte=0
        ).order_by(
            '-total_comments')[:count]


@register.inclusion_tag('blog/_unapproved_comments.html')
def get_unapproved_comments():
    """ Display list of posts with comments waiting for approval """
    # Retrieve all unapproved comments
    unapproved_comments = Comment.objects.filter(approved_comment=False)
    # Factor out duplicate posts (from multiple open comments)
    raw_posts_to_approve = []
    for comment in unapproved_comments:
        raw_posts_to_approve.append(comment.post_id)
    post_ids = list(set(raw_posts_to_approve))
    # List of Post IDs
    posts_to_approve = Post.published.filter(id__in=post_ids)
    return {'posts_to_approve': posts_to_approve}


@register.simple_tag
def total_unapproved_comments():
    """ Display count of comments needing approval """
    posts = get_unapproved_comments()['posts_to_approve']
    number = len(posts)
    return number
