from . import views

from django.urls import path 

app_name = 'lib'

urlpatterns = [

    

    path("", views.stor , name= 'store'),

    path("login", views.user_login ,name= 'login'),

    path("logout", views.user_logout ,name= 'logout'),

    path("index/", views.index , name= 'index'),

    path("Books/", views.home , name= 'Books'),

    path('index_cat/<int:id>/', views.index_cat, name='index_cat'),

    path('success_page/', views.success, name='success_page'),

    path('Books/delete/<int:id>/', views.delete, name='delete'),

    path('Books/update/<int:id>/', views.update, name='update'),

    path('Books/buying/<int:id>/', views.Book_buy,name= 'buying'),

]
