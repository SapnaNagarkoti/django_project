from django.urls import path
from django.conf.urls.static import static
from.import views

urlpatterns=[
    path('index',views.index, name='index'),
    path('add-blog',views.add_blog_post,name='add_blog_post'),
    path('blog-detail',views.blog_post_detail,name='blog_post_detail'),
    path('update-blog/<str:id>',views.update_blog_post,name='update_blog_post'),
    path('delete-blog/<str:id>',views.delete_blog_post,name='delete_blog_post'),
    path('view-blog/<str:id>',views.view_blog,name='view_blog'),
    path('add-comment/<str:id>',views.add_comment,name='add_comment'),
    path('delete-comment/<str:id>',views.delete_comment,name='delete_comment'),
    path('edit-comment/<str:id>',views.edit_comment,name='edit_comment'),
   ]



