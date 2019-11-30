from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from .emails import send_welcome_email


@login_required
def home(request):
    posts = Post.objects.all()
    hoods = Neighborhood.objects.all()
    businesses = Business.objects.all()
    context = {
        "posts":posts,
        "hoods":hoods,
        "businesses":businesses,
    }
    return render(request, 'index.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()

            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password1=form.cleaned_data['password1']
            recipient=User(username=username,email=email)
            try:
                send_welcome_email(username,email)
                messages.success(request, f'Account has been created successfully!')
            except:
                print('error')
            return redirect('/login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'users/register.html', context)


@login_required

def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'user_form':user_form,
    'profile_form':profile_form,
    }
    return render(request, 'profile.html', context)

def hood(request):
    profile = Profile.objects.all()
    context = {
        "profile":profile,
    }
    return render(request, 'navbar.html', context)


@login_required
def updateprofile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'user_form':user_form,
    'profile_form':profile_form,
    }

    return render(request, 'updateprofile.html', context)


@login_required
def createhood(request):
    current_user = request.user
    if request.method == 'POST':
        hood_form = NeighborhoodForm(request.POST, request.FILES)
        if hood_form.is_valid():
            post = hood_form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('/')
    else:
        hood_form = NeighborhoodForm()
    context = {
        "hood_form":hood_form,
    }
    return render(request, 'hood.html', context)


@login_required
def createbusiness(request):
    current_user = request.user
    if request.method == 'POST':
        business_form = BusinessForm(request.POST, request.FILES)
        if business_form.is_valid():
            post = business_form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('/')
    else:
        business_form = BusinessForm()
    context = {
        "business_form":business_form,
    }
    return render(request, 'business.html', context)
