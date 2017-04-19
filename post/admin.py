from django.contrib import admin

from post.models import Category, Post

# Register your models here.
admin.site.register(Category)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'content')
