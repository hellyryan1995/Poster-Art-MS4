from django.urls import path
from . import views

from blog.views import post_detail

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', post_detail, name='post_detail'),

]
