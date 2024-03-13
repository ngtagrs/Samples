from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class Thread(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("タイトル", default="New", max_length=128)
    created_by = models.ForeignKey(User,
                                   verbose_name="作成者",
                                   related_name="threads",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

class Chat(models.Model):
    name = models.CharField("送信者", max_length=128)
    message = models.TextField("メッセージ")
    thread = models.ForeignKey(Thread, 
                               verbose_name="スレッド", 
                               related_name="chats",
                               on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,
                                   verbose_name="作成者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
