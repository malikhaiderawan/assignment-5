from django.shortcuts import render
from .models import blogpost

def blog_post_list(request):
    posts = blogpost.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def blog_post_detail(request, pk):
    post = blogpost.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})
