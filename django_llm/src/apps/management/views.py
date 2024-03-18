from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from .models import Document, DocumentGroup
import os
from lib.llama_index.agent import ChatAgent

def pdf_list(request):
    pdfs = Document.objects.all()
    groups = DocumentGroup.objects.filter(created_by=request.user)
    return render(request, 'management/index.html', {'pdfs': pdfs, 'groups':groups})

def upload_pdf(request):
    if request.method == 'POST':
        with ChatAgent() as llamaindex_agent:
            for file in request.FILES.getlist('pdf_files'):
                new_pdf = Document(name=file.name, document=file, created_by=request.user)
                new_pdf.save()
                llamaindex_agent.add_new_document(f"media/pdfs/${file.name}")
    return redirect('management:pdf_list')

def delete_pdf(request, pdf_id):
    pdf = get_object_or_404(Document, pk=pdf_id)
    if request.method == 'POST':
        file_path = os.path.join(settings.MEDIA_ROOT, str(pdf.document))
        if os.path.exists(file_path):
            os.remove(file_path)
            pdf.delete()
            return JsonResponse({'message': 'PDFを削除しました。'}, status=200)
        else:
            return JsonResponse({'error': 'ファイルが見つかりません。'}, status=404)