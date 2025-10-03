from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.userRegister, name="userRegister"),
    path("login/", views.userLogin, name="userLogin"),
    path("logout/", views.userLogout, name="userLogout"),
]