from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    document = models.FileField(upload_to='pdfs/')
    groups = models.ManyToManyField('DocumentGroup', related_name='documents', verbose_name="グループ")
    created_by = models.ForeignKey(User,
                                   verbose_name="作成者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("作成日", auto_now_add=True)

    def __str__(self):
        return self.name
    
class DocumentGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    #documents = models.ManyToManyField('Document', related_name='groups', verbose_name="ドキュメント")
    created_by = models.ForeignKey(User,
                                   verbose_name="作成者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("作成日", auto_now_add=True)

    def __str__(self):
        return self.name