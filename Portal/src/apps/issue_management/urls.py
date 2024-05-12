from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="issue_main"),
    path("detail/<int:issue_id>", views.detail, name="issue_detail"),
    path("detail/delete_issue/<int:issue_id>", views.delete_issue, name="delete_issue"),
    path("detail/delete_issue_comment/<int:issue_comment_id>", views.delete_issue_comment, name="delete_issue_comment"),
]