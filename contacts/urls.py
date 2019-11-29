from django.urls import  path

from . import views

urlpatterns = [
    path('contact', views.contact, name= 'contact'),
    path('mycontact', views.mycontact, name= 'contact1'),
    path('<int:id>', views.message, name='message'),
    path('receive', views.receive, name='receive'),

]