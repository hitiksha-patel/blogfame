from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.index, name = 'index' ),
    path('user_register',views.user_register, name = 'user_register'),
    path('user_login',views.user_login, name = 'user_login'),
    path('user_logout',views.user_logout, name = 'user_logout'),
    path('blog_details',views.blog_details, name = 'blog_details'),
    path('verify/<token>', views.verify_mail, name = 'verify'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('Change_password/<token>', views.Change_password, name='Change_password'),
]