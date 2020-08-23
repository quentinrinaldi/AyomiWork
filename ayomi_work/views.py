from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
import json
from django.http import JsonResponse
from django.template.loader import render_to_string


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def update_profile(request):
    args = {}
# ONLY POST METHOD IS ACCEPTED. THE FORM IS DIRECTLY IN THE TEMPLATE
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            args['new_email'] = form.cleaned_data.get('email')
            args['success'] = True
            return JsonResponse(args);
        else:
            #IF FORM IS INVALID, JUST RETURN THE ERRORS THROUGHOUT THE TEMPLATE UPDATE_PROFILE_ERRORS
            args['content'] = render_to_string("update_profile_errors.html", {'form': form})
            args['success'] = False
            return JsonResponse(args);