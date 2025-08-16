# contact/urls.py
from django.urls import path
from .views import contact, done
app_name = "contact"
urlpatterns = [path("", contact, name="form"), path("done/", done, name="done")]

