from django.urls import  path

from . import views

urlpatterns =[
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('register1', views.register1, name='register1'),
    path('logout', views.logout , name='logout'),
    path('dashboard', views.dashboard , name='dashboard'),
    path('receive', views.receive , name='receive'),
    path('profile', views.profile , name='profile'),
    path('<int:id>', views.message, name='message'),


]
