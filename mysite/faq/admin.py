from django.contrib import admin
from .models import Post, Category

admin.site.site_header = "FAQ Administration"
admin.site.site_title = "FAQ Admin Portal"
admin.site.index_title = "Welcome to the FAQ Administration"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','question', 'username', 'email', 'author', 'publish', 'status', 'ticket')
    list_filter = ('status', 'created', 'publish', 'author', 'ticket')
    search_fields = ('title', 'body', 'username', 'email')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
