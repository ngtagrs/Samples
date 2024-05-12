from django.db import models
from django.conf import settings
from django_currentuser.db.models import CurrentUserField


class IssueCategory(models.Model):
    """案件の分類"""
    category = models.CharField("分類", max_length=32, primary_key=True)

    def __str__(self):
        return self.category

class IssueStatus(models.Model):
    """案件のステータス"""
    status = models.CharField("ステータス", max_length=8, primary_key=True)

    def __str__(self):
        return self.status
    
class Issue(models.Model):
    """案件"""
    id = models.AutoField("ID", auto_created=True, primary_key=True)
    category = models.ForeignKey(IssueCategory,
                                 verbose_name="案件分類",
                                 on_delete=models.SET_DEFAULT,
                               default="未選択")
    title = models.CharField("タイトル", max_length=128)
    description = models.TextField("説明")
    status = models.ForeignKey(IssueStatus,
                               verbose_name="ステータス",
                               on_delete=models.SET_DEFAULT,
                               default="完了")
    pic = models.ForeignKey(settings.AUTH_USER_MODEL,
                            verbose_name="担当者",
                            on_delete=models.DO_NOTHING,
                            related_name="in_charge_issue")
    registered_at = models.DateTimeField("登録日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    registered_by = CurrentUserField(settings.AUTH_USER_MODEL,
                                  verbose_name="登録者",
                                  on_delete=models.DO_NOTHING,
                            related_name="registered_issue")
    updated_by = CurrentUserField(settings.AUTH_USER_MODEL,
                                  verbose_name="更新者",
                                  on_delete=models.DO_NOTHING,
                                  related_name="updated_issue")
    #comments:List[IssueComment]
    #file = models.FileField(upload_to)
    def __str__(self):
        return self.title
    
class IssueComment(models.Model):
    """案件に対するコメント"""
    id = models.AutoField("ID", auto_created=True, primary_key=True)
    comment = models.TextField("コメント")
    issue = models.ForeignKey(Issue,
                              verbose_name="案件",
                              on_delete=models.CASCADE,
                              related_name="comments")
    #files:List[object]
    posted_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    posted_by = CurrentUserField(settings.AUTH_USER_MODEL,
                                  verbose_name="投稿者",
                                  on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"{self.issue.title}_comment_{self.id}"
