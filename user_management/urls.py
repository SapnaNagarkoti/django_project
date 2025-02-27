from django.urls import path
from.import views
from.import test

urlpatterns=[
    path('',views.index ,name='index'),
    path('user-login',views.user_login,name='user_login'),
    path('user-logout',views.user_logout,name='user_logout'),
    path('user-list',views.user_list,name='user_list'),
    path('user-update/<str:id>',views.update_user,name='update_user'),
    path('user-delete/<str:id>',views.delete_user,name='delete_user'),
    path('follow_author',views.follow_author,name='follow_author'),
    path('user-profile/<str:id>',views.view_profile,name='view_profile'),
    path('webhook',test.webhook_verify,name='webhook_verify'),

]
