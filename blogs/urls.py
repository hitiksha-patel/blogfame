from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('',views.index, name = 'index' ),
    path('create_blog/',views.create_blog, name = 'create_blog' ),
    path('show_blog/',views.show_blog, name = 'show_blog' ),
    path('blog_details/<int:id>/',views.blog_details, name = 'blog_details' ),
    path('delete_blog/<int:id>/',views.delete_blog, name = 'delete_blog' ),
    path('update_blog/<int:id>/',views.update_blog, name = 'update_blog' ),
    path('my_blogs/',views.my_blogs, name = 'my_blogs'),
    path('my_profile',views.my_profile, name = 'my_profile' ),
    path('change_user_password',views.change_user_password, name = 'change_user_password' ),
    path('update_profile',views.update_profile, name = 'update_profile' ),
]