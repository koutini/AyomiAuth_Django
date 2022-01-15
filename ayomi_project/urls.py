"""ayomi_project URL Configuration"""
from django.contrib import admin
from django.urls import path

from ayomi_auth.views import RegisterView, LoginView, LogoutView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RegisterView, name="register"),
    path('login/', LoginView, name="login"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('logout/', LogoutView, name="logout"),
]
