from django.urls import path
from chat_bot import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "chat_bot"
urlpatterns = [
    path("", views.index, name="chat_bot"),
    path("<int:thread_id>/", views.chat, name="chat_thread"),
    path("gpt/<int:thread_id>/", views.ChatGPTStreamView.as_view(), name="gpt"),
    path("delete/<int:thread_id>/", views.delete_thread, name="delete_thread"),
    path("rename/<int:thread_id>/", views.rename_thread, name="rename_thread"),
    path("add_new_thread/", views.add_new_thread, name="add_new_thread"),
    path("add_chat_history/<int:thread_id>/", views.add_chat_history, name="add_chat_history"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)