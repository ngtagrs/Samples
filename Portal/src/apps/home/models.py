from django.db import models
from django.conf import settings
from django_currentuser.db.models import CurrentUserField

class Action(models.Model):
    """Action"""
    page = models.CharField("分類", max_length=32, primary_key=True)
    type = models.CharField("タイプ", max_length=32)
    description = models.TextField()
    created_at = models.DateTimeField("更新日", auto_now_add=True)
    created_by = CurrentUserField(settings.AUTH_USER_MODEL,
                                  verbose_name="更新者",
                                  on_delete=models.DO_NOTHING,
                                  related_name="action_user")