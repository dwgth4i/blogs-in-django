from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.
def index(request):
    return render(request,'faq/index.html')

def about(request):
    return render(request, 'faq/about.html')

def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-publish')
    return render(request, 'faq/post_list.html', {'posts': posts})

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'faq/post_detail.html', {'post': post})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category, status='published').order_by('-publish')
    return render(request, 'faq/category_list.html', {'category': category, 'posts': posts})