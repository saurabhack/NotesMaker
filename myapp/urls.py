from django.urls import path,include
from . import views
urlpatterns=[
    path('', views.index,name='index'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('AddNote',views.AddNote,name="AddNote"),
    path('del/<str:item_id>', views.delete,name='del'),
    path('show/<str:item_id>', views.show, name='show'),
    path('search',views.search_result,name='search'),
]
