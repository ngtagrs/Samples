from django.contrib import admin
from apps.issue_management.models import (
    Issue,
    IssueCategory,
    IssueStatus,
    IssueComment
)

admin.site.register(Issue)
admin.site.register(IssueCategory)
admin.site.register(IssueStatus)
admin.site.register(IssueComment)
