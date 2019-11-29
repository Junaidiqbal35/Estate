from django.urls import  path

from . import views

urlpatterns =[
    path('', views.index, name='listings'),
   # path('create', views.create, name='create'),
    path('addSpace', views.addspace, name='addspace'),
    path('rating', views.myindex, name='rating'),



    path('<int:id>', views.listing, name='listing'),
    #path('<int:id>', views.listing1, name='listing1'),
    path('mylisting', views.mylisting, name='mylisting'),
    path('search', views.search , name='search'),
  #  path('edit/<int:id>',views.edit, name='edit'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.delete , name='delete'),
    #path('<int:id>/comment/',views.add_comment_to_listing , name='add_comment_to_listing'),
    path('<id>/favourite_listing', views.favourite, name='favourite'),
    path('board/', views.board, name='board'),
    path('photoshoot/', views.photoShoot_Search , name='photoshoot'),
    path('birthdayParty/', views.birthday_Search , name='birthday'),
    path('workshop/', views.workshop_Search , name='workshop'),
    path('bridalShower/', views.bridalShower_Search , name='bridal'),
    path('meeting/', views.meeting_Search , name='meeting'),
    path('weddingDestination/', views.wedding_Search , name='wedding'),

]
