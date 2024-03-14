from django.urls import path
from chat_bot import views

app_name = "chat_bot"
urlpatterns = [
    path("", views.index, name="chat_bot"),
    path("<int:thread_id>/", views.chat, name="chat_thread"),
    path("gpt/<int:thread_id>/", views.request_gpt, name="gpt"),
    path("delete/<int:thread_id>/", views.delete_thread, name="delete_thread")
]