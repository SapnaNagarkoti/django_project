from user_management.models import customuser
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class blog_post(models.Model):
    title = models.CharField(default=None,null=True)
    description = CKEditor5Field('description', config_name='extends',default=None,null=True)# CKEditor Rich Text Fiel
    image = models.ImageField(upload_to='image')
    author = models.ForeignKey(customuser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blog_post'

    def __str__(self):
        return f"{self.title}"

class post_comment(models.Model):
    comment = models.CharField(default=None,null=True)
    blog = models.ForeignKey(blog_post,on_delete=models.CASCADE ,null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'post_comment'

