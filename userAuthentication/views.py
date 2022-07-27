from multiprocessing import context
from django.shortcuts import render
from .forms import UserForm, UserInfoForm, ImageForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .models import UserInfo



# Create your views here.
def loginPage(request):
    return render(request, 'userAuthentication/login.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('user-password')
        user = authenticate(username=username, password=password)
        if user is not None:  #to check whether user is available or not?
            # the password verified for the user
            if user.is_active:   
                login(request, user)
                return HttpResponseRedirect(reverse('homeApp:home-page'))
            else:
                return HttpResponse("The password is valid, but the account has been disabled!")
        else:
            return HttpResponse("The password or user is invalid.")
    else:
        return HttpResponseRedirect(reverse('userAuthentication:login-page'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homeApp:home-page'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)
        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user
            if 'profile_image' in request.FILES:
                user_info.profile_image = request.FILES['profile_image']
            
            user_info.save()
            registered = True

    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()
    context = {
        'title':'Register',
        'user_form':user_form,
        'user_info_form':user_info_form,
        'registered':registered
    }
    return render(request, 'userAuthentication/register.html', context=context)

@login_required
def profile(request):
    context = {}
    if request.user.is_authenticated:
        current_user = request.user
        current_user_full_name = request.user.get_full_name()
        current_user_id = current_user.id
        user_basic_info = User.objects.get(pk=current_user_id)
        user_more_info = UserInfo.objects.get(user_id=current_user_id)
        form = ImageForm(instance=request.user)
        context = {'full_name': current_user_full_name, 'user_basic_info':user_basic_info, 'user_more_info':user_more_info, 'form':form}
    return render(request, 'userAuthentication/profile.html', context=context)

@login_required
def update_profile(request, id):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        gender = request.POST['gender']
        facebook_link = request.POST['facebook_link']
        user_basic_info = User.objects.get(pk=id)
        user_more_info = UserInfo.objects.get(user_id=id)
        user_basic_info.username = username
        user_basic_info.first_name = first_name
        user_basic_info.last_name = last_name
        user_basic_info.email = email
        user_more_info.gender = gender
        user_more_info.facebook_id = facebook_link
        user_basic_info.save()
        user_more_info.save()
    return HttpResponseRedirect(reverse('userAuthentication:profile'))

def set_profile_image(request, id):
    if request.method == 'POST':
        user_info = UserInfo.objects.get(user=request.user)
        form = ImageForm(request.POST,request.FILES,instance=user_info)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('userAuthentication:profile'))
    return HttpResponseRedirect(reverse('userAuthentication:profile'))
    