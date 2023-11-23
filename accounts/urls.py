from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/',views.login,name='login'),
    path('logout/', views.logout, name= 'logout'),
    path('profile/',views.profile,name='profile'),
    path('aboutus/',views.aboutus,name='aboutus'),

    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('resetpassword_validate/<uidb64>/<token>/',views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
]
