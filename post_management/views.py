from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from.models import blog_post
from .forms import blogform, commentform
from.models import post_comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user_management.models import customuser

from django.conf import settings

base_url = settings.BASE_URL


# Create your views here.
def index(request):
    return HttpResponse("success")

@login_required(login_url='user_login')
def add_blog_post(request):
    if request.method=='POST':
        data = blogform(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            return render(request,'blog.html')
        else:
            print('invalid data')
    else:
        data = blogform(request.POST, request.FILES)
        return render(request,'add-blog.html',{'data':data})


@login_required(login_url='user_login')
def blog_post_detail(request):
   post_data = blog_post.objects.all()
   print(post_data)
   messages.success(request,'blog detail found')
   return render(request,'blog.html',{'data':post_data})


@login_required(login_url='user_login')
def update_blog_post(request,id):
    current_data = blog_post.objects.filter(id=id).first()
    if request.method == 'POST':
        data = blogform(request.POST,request.FILES ,instance = current_data)
        if data.is_valid():
            data.save()
            return redirect('blog_post_detail')
        else:
            print("data is invalid")
    else:
        form = blogform(instance = current_data)
    return render(request,'update-blog.html',{'id':id ,'data':form})

@login_required(login_url='user_login')
def delete_blog_post(request,id):
    data=blog_post.objects.filter(id=id).first()
    data.delete()
    return redirect('blog_post_detail')

@login_required(login_url='user_login')
def view_blog(request,id):
    data=blog_post.objects.filter(id=id).first()
    comment=post_comment.objects.filter(blog_id=id)
    print(comment)
    return render(request,'view-blog.html',{'data':data,'comment':comment})

@login_required(login_url='user_login')
def add_comment(request,id):
    # data = blog_post.objects.filter(blog_id=id)
    # comment = post_comment.objects.filter(blog_id=id).first()
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            post_comment.objects.create(comment=comment_text,blog_id=id)
            return redirect('view_blog',id)
        else:
            return HttpResponse("Invalid data")
    else:
        return HttpResponse("get method")

def delete_comment(request,id):
    data = post_comment.objects.filter(id=id).first()
    data.delete()
    return HttpResponse('success')

def edit_comment(request,id):
    comment = post_comment.objects.filter(id=id).first()
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            post_comment.objects.create(comment=comment_text)
            return redirect('view_blog',id)
        else:
            return HttpResponse("invalid data")
    else:
        comment = post_comment.objects.filter(id=id).first()
        return render(request,'update-comment.html',{'comment':comment,})

