from django.urls import path
from . import views

urlpatterns = [
    # path('<int:userid>', views.index, name='index'),
    path('home', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('recom', views.recom, name='recom'),

]
