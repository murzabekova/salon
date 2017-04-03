from django.contrib import admin
from post.models import Post
from post.models import Category

# Register your models here.
admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'category')

#admin.site.register(Post)
