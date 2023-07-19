from django.urls import path
from . import views
urlpatterns=[
    path('', views.index,name='index'),
    path('register',views.regiser,name='register'),
    path('logout',views.logout,name='logout'),
    path('AddNote',views.AddNote,name="AddNote"),
]
