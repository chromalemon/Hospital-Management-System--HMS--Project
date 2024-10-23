from login import views
from django.urls import path, include


app_name = "login"
urlpatterns = [
    path("login", views.login, name="login"),
    path("patient", views.patientLogin, name="patientLogin"),
    path("patient/process/<intDOB>", views.patientProcess, name="patientProcess"),
    path("staff", views.staffLogin, name="staffLogin"),
]