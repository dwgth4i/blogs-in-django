from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post, Category
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, PostForm, CommentForm

def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-publish')
    return render(request, 'faq/post_list.html', {'posts': posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', year=post.publish.year, month=post.publish.month, day=post.publish.day, slug=post.slug)
    else:
        comment_form = CommentForm()

    return render(request, 'faq/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.status = 'draft'
            question.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'faq/ask_question.html', {'form': form})

@login_required
def answer_question(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user and not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to answer this question.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.status = 'published'
            post.answered = True
            post.save()
            return redirect('post_detail', year=post.publish.year, month=post.publish.month, day=post.publish.day, slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'faq/answer_question.html', {'form': form})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category, status='published').order_by('-publish')
    return render(request, 'faq/category_list.html', {'category': category, 'posts': posts})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = SignUpForm()
    return render(request, 'faq/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'faq/signin.html', {'form': form})

from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordResetForm

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
    email_template_name = 'registration/password_reset_email.html'