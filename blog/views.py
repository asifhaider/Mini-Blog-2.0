from django.shortcuts import render
# from django.http import HttpResponse
 
# Create your views here.

posts = [
    {
        'author': 'Asif',
        'title': 'Blog Post 1',
        'content': 'First Post Content, Extreme Lorum Epsum',
        'date': 'September 13, 2020'
    },
    {
        'author': 'Elhan',
        'title': 'Blog Post 2',
        'content': 'Second Post Content, Extreme Lorum Epsum',
        'date': 'September 14, 2020'
    }
    
]


def home (request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)

def about (request):
    return render (request, 'blog/about.html')