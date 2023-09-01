from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Post, Comment
from .forms import CommentForm
from django.db.models import Q

import requests
from django.http import JsonResponse

def index(request):
    post = Post.objects.order_by ('-edit_date').all()
    return render (request, template_name='recipes_blog/index_post.html', context={'post': post})


class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "recipes_blog/create_post.html"
    success_url = reverse_lazy('blog_index')
    fields = [
        "title","description","image","recipe_country"
    ]
    permission_required = "post.add_post"    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = "recipes_blog/delete_post.html"
    success_url = reverse_lazy('blog_index')

class UpdatePost(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = "recipes_blog/update_post.html"
    success_url = reverse_lazy('blog_index')
    fields = [
        "title","description","image","recipe_country"
    ]
   
def DetailPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('detail_post', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'recipes_blog/detail_post.html', {'post': post, 'comments': comments, 'form': form})

class ListPost(LoginRequiredMixin,ListView):
    model = Post

def get_countries_by_name(request, country_name):
    url = 'https://restcountries.com/v3.1/name/{0}?fields=name'.format(country_name)
    response = requests.get(url, headers={'Content-Type': 'application/json'})
    data = response.json()
    print(data)
    return JsonResponse(data, safe=False)

class SearchPost(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'recipes_blog/search_post.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query))
        return object_list