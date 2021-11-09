from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('account/', views.accountSettings, name="account"),

    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name = "user-page"),
    path('userpageform/<str:pk_test>/', views.userPageform, name = "userpageform"),
    path('userrepairform/<str:pk_test>/', views.userrepairPageform, name = "userrepairpageform"),
    path('welcome', views.home, name="home"),
    path('employee/<str:pk_test>/', views.customer, name="employee"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),



    
]