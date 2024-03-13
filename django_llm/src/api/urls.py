from django.urls import path
from api import views

app_name = "api"
urlpatterns = [
    path("gpt/", views.request_gpt, name="gpt")
]