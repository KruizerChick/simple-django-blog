""" Views for Blog app """
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
class PostListView(ListView):
    """ Lists published posts only """
    model = Post

    def get_queryset(self):
        # Only show current and past posts
        return Post.objects.filter(
            published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    """ Blog post detail """
    model = Post
    success_url = reverse_lazy('blog:post_list')


class CreatePostView(LoginRequiredMixin, CreateView):
    """ New blog post """
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """ Updates existing blog post """
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class DraftListView(LoginRequiredMixin, ListView):
    """ Lists draft posts, not published yet """
    login_url = '/login/'
    # redirect_field_name = 'blog/post_list.html'
    redirect_field_name = 'blog/post_draft_list.html'
    model = Post
    template_name = 'blog/post_draft_list.html'

    def get_queryset(self):
        """ Display only draft posts from the current user """
        return Post.objects.filter(
            published_date__isnull=True, author=self.request.user
            ).order_by('created_date')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """ Deletes existing blog post """
    model = Post
    success_url = reverse_lazy('blog:post_list')

#######################################
## Functions that require a pk match ##
#######################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog:post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail', pk=post_pk)
