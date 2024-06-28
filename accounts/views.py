from django.shortcuts import render, redirect
from . forms import *
from django.contrib.auth import authenticate , login, logout
from blogs.models import Blog
from django.contrib import messages
import uuid
from .helper import send_verify_mail, forgot_password_mail
# Create your views here.

def index(request):
    show_blogs = Blog.objects.all()
    if request.user.is_authenticated:
        return redirect('blogs:index')
    return render(request, 'accounts/index.html',{'show_blogs':show_blogs})

def user_register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            token = str(uuid.uuid4())
            user.email_token = token
            user.save()
            send_verify_mail(user.email, token)
            messages.success(request, "Please check your email and verify your account to login!")
            return redirect('accounts:user_login')
        else:
            print(form.errors)
    else:
        form = UserRegister()
    return render(request, 'accounts/register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user:
            if user.is_verified:
                login(request,user)
                return redirect('blogs:index')
            else:
                messages.success(request, "Please verify your account to login!")
                return redirect('accounts:user_login')
        else:
            messages.success(request, "Invalid Credentials!")
            return redirect('accounts:user_login')
    return render(request, 'accounts/login.html')


def verify_mail(request, token):
    try:
        user = User.objects.filter(email_token= token).first()

        if user:
            if user.is_verified:
                messages.success(request, "You have already verified you account!")
                return redirect('accounts:user_login')
            
            user.is_verified = True
            user.save()
            messages.success(request, "Congratz! You have verified you account!")
            return redirect('accounts:user_login')
        
        else:
            messages.success(request, "Invalid verification link!")
            return redirect('accounts:user_login')

    except Exception as e:
        print(e)


def user_logout(request):
    logout(request)
    return redirect('accounts:index')

def blog_details(request,id):
    details = Blog.objects.get(id=id)
    return render(request, 'blogs/details.html',{'details':details})

def forgot_password(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')

            user = User.objects.filter(email=email).first()
            if user:
                user_email = User.objects.get(email=email)
                token = str(uuid.uuid4())
                user_ = User.objects.get(email = user)
                user_.forgot_password_token = token
                user_.save()
                forgot_password_mail(user_email, token)
                messages.success(request, 'Please check your mail!')
                return HttpResponseRedirect(reverse('accounts:forgot_password'))
            else:
                messages.success(request, 'No user found with this email address!')
                return redirect('accounts:forgot_password')
    except Exception as e:
        print(e)
    return render(request, 'accounts/forgot_password.html')


def Change_password(request, token):
    try:
        user = User.objects.filter(forgot_password_token=token).first()
        if user is None:
            messages.success(request, 'This link is not valid anymore! ')
            return HttpResponseRedirect(reverse('accounts:Change_Password'))



        if request.method == 'POST':
            new_password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            user_id = user.id

            if user_id is None:
                messages.success(request, 'No user id Found')
                return HttpResponseRedirect(reverse(f'accounts:Change_Password/{token}'))
            
            if new_password != confirm_password:
                messages.success(request, 'Password and Confirm password Should be same!')
                return HttpResponseRedirect(reverse(f'accounts:Change_Password/{token}'))

            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.forgot_password_token = None
            user_obj.save()
            messages.success(request, 'Your Password has been changed!')
            return HttpResponseRedirect(reverse('accounts:user_login'))

    except Exception as e:
        print(e)
    return render(request, 'accounts/forgot-password.html')
