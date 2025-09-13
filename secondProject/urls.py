"""
URL configuration for secondProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nav/', views.nav, name='nav'),
    path('', views.register),
    path('about/', views.about),
    path('contact/', views.contact),
    path('candidate/', views.candidate_view, name='candidate'),
    path("result/", views.result_view, name="result"),
    path("admitcard/", views.admitcard_view, name="admitcard"),
    path("index/", views.index_view, name="index"), 
    path("resume/", views.resume_view, name="resume"),
    path("post/", views.post_view, name="post"),
    path('registration/', views.register, name='registration'),
    path('preview/', views.preview, name='preview'),
    path('marksheet_form/', views.marksheet_form, name='marksheet_form'),
    path('display_marksheet/', views.display_marksheet, name='display_marksheet'),
      # URL for the input form page
    # path('marksheet', views.marksheet_form, name='marksheet_form'),
    # # URL for the result/marksheet page
    # path('result/', views.display_marksheet, name='display_marksheet'),
]




from django.shortcuts import render, redirect