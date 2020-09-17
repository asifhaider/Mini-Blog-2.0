from django.shortcuts import render
from .models import Post

from django.views.generic import (ListView, 
                                DetailView, 
                                CreateView, 
                                UpdateView, 
                                DeleteView
                                ) # for trying out Class based views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# from django.http import HttpResponse
 
# Create your views here.

#### DUMMY POST DATA, REMOVED LATER 

# posts = [
#     {
#         'author': 'Asif',
#         'title': 'Blog Post 1',
#         'content': 'First Post Content, Extreme Lorum Epsum',
#         'date': 'September 13, 2020'
#     },
#     {
#         'author': 'Elhan',
#         'title': 'Blog Post 2',
#         'content': 'Second Post Content, Extreme Lorum Epsum',
#         'date': 'September 14, 2020'
#     }
    
# ]

# function view

def home (request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context)

def about (request):
    return render (request, 'blog/about.html')

# class view

class PostListView (ListView):
    model = Post
    template_name = 'blog/home.html' # search for <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # new attribute for ordering out, minus for altering order 

class PostDetailView (DetailView):
    model = Post

class PostCreateView (LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView (LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    


