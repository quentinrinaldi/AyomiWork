from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            response = HttpResponse()
            response['new_email'] = form.cleaned_data.get('email')
            return response
    else:
        form = UpdateProfileForm()
    args['form'] = form
    return render(request, 'update_profile.html', args)