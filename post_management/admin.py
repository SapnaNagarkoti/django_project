from django.contrib import admin
from.models import blog_post,post_comment

# Register your models here.
admin.site.register(blog_post)
admin.site.register(post_comment)