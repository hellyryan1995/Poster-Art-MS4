from django.urls import path
from . import views

from blog.views import post_detail

urlpatterns = [
    path('', views.blog, name='blog'),
    path('int:<post_id>/', post_detail, name='post_detail'),
    path('add/', views.add_post , name='add_post'),

]
