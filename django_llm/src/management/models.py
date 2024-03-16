from django.db import models

# Create your models here.
class PDFDocument(models.Model):
    name = models.CharField(max_length=255)
    document = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.name