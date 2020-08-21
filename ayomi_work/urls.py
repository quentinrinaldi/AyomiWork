from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('userAccount/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('userAccount/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('userAccount/profile', login_required(TemplateView.as_view(template_name='profile.html')), name="profile"),
    path('userAccount/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup')

]