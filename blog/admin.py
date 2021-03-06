from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'create_time', 'author']


admin.site.register(Post, PostAdmin)
