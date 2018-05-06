""" Feeds for Blog app """
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post


class LatestPostsFeed(Feed):
    """ Blog feed """
    title = 'My Blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self):
        """ Returns the last 5 posts """
        return Post.objects.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)