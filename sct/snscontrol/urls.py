from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('add_post/', views.add_post, name='add_post'),
    path('view_post/', views.view_post, name="view_post"),
    path('master_post/', views.master_post, name="master_post"),
    path('approve_post/<int:pk>/', views.approve_post, name="approve_post"),
]