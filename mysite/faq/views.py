from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
from .forms import CommentForm

def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-publish')
    return render(request, 'faq/post_list.html', {'posts': posts})

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'faq/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category, status='published').order_by('-publish')
    return render(request, 'faq/category_list.html', {'category': category, 'posts': posts})
