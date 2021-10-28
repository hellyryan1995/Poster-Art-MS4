from django.urls import path
from . import views
from home.views import about


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', about, name='about'),
]
