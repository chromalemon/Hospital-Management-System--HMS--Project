from login import views
from django.urls import path


app_name = "login"
urlpatterns = [
    path("", views.home, name="home"),
]