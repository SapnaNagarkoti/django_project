from django import forms
from .models import blog_post, post_comment
from user_management.models import customuser
from django_ckeditor_5.widgets import CKEditor5Widget

class blogform(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title','max_length':100}))
    description = forms.CharField(
        widget=CKEditor5Widget(attrs={
            'class': 'ckeditor',
        })
    )
    image = forms.ImageField()
    author = forms.ModelChoiceField(
        queryset = customuser.objects.all(),
        empty_label="Select author",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = blog_post
        fields = ("title", "description","image","author")


class commentform(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Comment','max_length':50}))
    blog = forms.ModelChoiceField(
           queryset = blog_post.objects.all(),
           empty_label = 'Select Post',
           widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = post_comment
        fields =('comment','blog')