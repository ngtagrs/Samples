from django.urls import path
from management import views

app_name = "management"
urlpatterns = [
    path("", views.index, name="index"),
]