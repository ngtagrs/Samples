from django.urls import path
from . import views

app_name = "management"

urlpatterns = [
    path('', views.pdf_list, name='pdf_list'),
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('delete/<int:pdf_id>/', views.delete_pdf, name='delete_pdf'),
]