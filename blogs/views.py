from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .forms import *
from .models import Blog
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.


@login_required
def index(request):
    show_blogs = Blog.objects.all().order_by('-id')[:6]
    return render(request, 'blogs/index.html',{'show_blogs':show_blogs})


@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit = False)
            user.user = request.user
            user.save()
            return redirect('blogs:index')
        else:
            print(form.errors)
    else:
        form = BlogForm()
    return render(request, 'blogs/add_blog.html',{'form':form})


@login_required
def show_blog(request):
    show_blogs = Blog.objects.all()
    return render(request, 'blogs/all_blogs.html',{'show_blogs':show_blogs})


@login_required
def blog_details(request,id):
    details = Blog.objects.get(id=id)
    return render(request, 'blogs/details.html',{'details':details})


@login_required
def delete_blog(request,id):
    dele = Blog.objects.get(id=id)
    dele.delete()
    return redirect('blogs:show_blog')


@login_required
def update_blog(request,id):
    details = Blog.objects.get(id=id)
    form = UpdateBlogForm(request.POST or None, request.FILES or None,instance = details)
    if form.is_valid():
            form.save()
            print('hii')
            return redirect('blogs:show_blog')
    return render(request, 'blogs/update_blog.html',{'form':form})

@login_required
def my_blogs(request):
    my_blog = Blog.objects.filter(user_id = request.user.id )
    return render(request, 'blogs/my_blog.html',{'my_blog':my_blog})    

@login_required
def my_profile(request):
    user = User.objects.get(id=request.user.id)
    return render(request, 'blogs/my_profile.html',{'user':user})


@login_required
def update_profile(request):
    details = User.objects.get(id=request.user.id)
    form = UpdateProfileForm(request.POST or None, request.FILES or None,instance = details)
    if form.is_valid():
            form.save()
            print('hii')
            return redirect('blogs:my_profile')
    return render(request, 'blogs/update_profile.html',{'form':form})


@login_required
def change_user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('blogs:index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'blogs/change_password.html', {'form': form})





