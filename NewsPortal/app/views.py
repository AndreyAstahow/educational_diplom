from django.shortcuts import render
from django.views.generic import (
        ListView, DetailView, CreateView, DeleteView, UpdateView
    )
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import Post
from .forms import PostForm

class PostList(ListView):
    model = Post
    ordering = 'time_create'
    template_name = 'flatpages/post.html'
    context_object_name = 'post'
    paginate_by = 10

class ResponseList(LoginRequiredMixin, ListView):
    permission_required = ('NewsPortal.app')
    model = Post
    template_name = 'flatpages/response.html'
    context_object_name = 'response'

class PostCreate(LoginRequiredMixin, CreateView):
    permission_required = ('NewsPortal.app')
    form_class = PostForm
    model = Post
    template_name = 'flatpages/create_post.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.save()
        return super().form_valid(form)
    
class PostDetail(DetailView):
    model = Post
    ordering = 'author_id'
    template_name = 'flatpages/post_detail.html'
    context_object_name = 'post_detail'

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'flatpages/post_delete.html'
    success_url = reverse_lazy('post_list')

class PostUpdate(LoginRequiredMixin, UpdateView):
    permission_required = ('NewsPortal.change_post')
    form_class = PostForm
    model = Post
    template_name = 'flatpages/create_post.html'

@login_required
def response(request, pk):
    user = request.user
    post = Post.objects.get(pk=pk)
    post.response.add(user)
    return redirect('post_list')