from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register_user,name='register'),
    path('login/', views.user_login,name='login'),
    path('logout/', views.user_logout,name='logout'),
    path('change_password/', views.change_user_password,name='change_password'),
    path('set_password/', views.set_user_password,name='set_password'),
]
