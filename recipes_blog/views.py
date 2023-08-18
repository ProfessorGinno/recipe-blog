from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Post

# Create your views here.

def index(request):
    post = Post.objects.order_by ('-actualitation_date').all()
    return render (request, template_name='recipes_blog/index_post.html', context={'post': post})


class CreatePost(CreateView):
    model = Post
    template_name = "recipes_blog/create_post.html"
    success_url = reverse_lazy('home')
    fields = [
        "title","description","image","recipe_country"
    ]
    permission_required = "post.add_post"

class DeletePost(DeleteView):
    model = Post
    template_name = "recipes_blog/delete_post.html"
    success_url = reverse_lazy('home')
    # permission_required = "post.delete_post" 

class UpdatePost(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Post
    template_name = "recipes_blog/update_post.html"
    success_url = reverse_lazy('blog_index')
    fields = [
        "title","description","image","creation_date","actualitation_date","recipe_country"
    ]
    permission_required = "post.update_post" 

class DetailPost(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "recipes_blog/detail_post.html"

class ListPost(LoginRequiredMixin,ListView):
    model = Post