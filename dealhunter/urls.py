from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("new_deal", views.new_deal, name="new_deal"),
    
    path("logout_view", views.logout_view, name="logout_view"),
    path("deal/<int:deal_id>", views.dealview, name="dealview"),
    path("profile/<int:profile_id>", views.profileview, name="profileview"),
]