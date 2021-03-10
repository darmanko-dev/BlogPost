from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("register/",views.register_user, name = "register"),
    path("login/",  views.Login_view, name = 'login'),
    path("logout/" , LogoutView.as_view() , name="logout"),
    path("profile/",  views.profile, name = 'profile'),
]
