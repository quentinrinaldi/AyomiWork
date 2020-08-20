from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('userAccount/', include('django.contrib.auth.urls')),
    path('home', TemplateView.as_view(template_name='home.html'), name='home')

]