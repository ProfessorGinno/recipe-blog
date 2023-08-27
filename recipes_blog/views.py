from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Post

import requests
from django.http import JsonResponse

# Create your views here.

def index(request):
    post = Post.objects.order_by ('-actualitation_date').all()
    return render (request, template_name='recipes_blog/index_post.html', context={'post': post})


class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "recipes_blog/create_post.html"
    success_url = reverse_lazy('blog_index')
    fields = [
        "title","description","image","recipe_country"
    ]
    permission_required = "post.add_post"    

    # def __init__():
    #     # print('CREATE_POST_INIT')
    #     pass

class DeletePost(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = "recipes_blog/delete_post.html"
    success_url = reverse_lazy('blog_index')
    # permission_required = "post.delete_post" 

class UpdatePost(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = "recipes_blog/update_post.html"
    success_url = reverse_lazy('blog_index')
    fields = [
        "title","description","image","recipe_country"
    ]
    # permission_required = "post.update_post" 

class DetailPost(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "recipes_blog/detail_post.html"

class ListPost(LoginRequiredMixin,ListView):
    model = Post

def get_countries_by_name(request, country_name):
    url = 'https://restcountries.com/v3.1/name/{0}?fields=name'.format(country_name)
    response = requests.get(url, headers={'Content-Type': 'application/json'})
    data = response.json()
    print(data)
    return JsonResponse(data, safe=False)