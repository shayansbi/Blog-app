from django.contrib import admin

from .models import Post

from .models import Comment

class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
    list_display = [
        'title',
        'body',
        'author'
    ]

admin.site.register(Post, PostAdmin)