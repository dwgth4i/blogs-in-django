from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    question = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    username = models.CharField(max_length=80, default='Anonymous')
    email = models.EmailField(default='anonymous@example.com')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='faq_posts', null=True, blank=True)
    body = models.TextField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    answered = models.BooleanField(default=False)

    def __str__(self):
        return self.question

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this field
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.post}'
