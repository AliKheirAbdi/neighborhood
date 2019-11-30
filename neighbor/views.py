from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *


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
