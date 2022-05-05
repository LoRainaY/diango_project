from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]
