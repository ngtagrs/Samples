from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
from .models import PDFDocument
import os

def pdf_list(request):
    pdfs = PDFDocument.objects.all()
    return render(request, 'management/index.html', {'pdfs': pdfs})

def upload_pdf(request):
    if request.method == 'POST':
        for file in request.FILES.getlist('pdf_files'):
            new_pdf = PDFDocument(name=file.name, document=file)
            new_pdf.save()
    return redirect('management:pdf_list')

def delete_pdf(request, pdf_id):
    pdf = get_object_or_404(PDFDocument, pk=pdf_id)
    if request.method == 'POST':
        file_path = os.path.join(settings.MEDIA_ROOT, str(pdf.document))
        if os.path.exists(file_path):
            os.remove(file_path)
            pdf.delete()
            return JsonResponse({'message': 'PDFを削除しました。'}, status=200)
        else:
            return JsonResponse({'error': 'ファイルが見つかりません。'}, status=404)