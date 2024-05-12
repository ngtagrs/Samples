from django import forms
from apps.issue_management.models import (
    Issue,
    IssueComment
)

class IssueForm(forms.ModelForm):
    class Meta:
         model = Issue
         fields = ['title', 'category', 'description', 'pic']

class CommentForm(forms.ModelForm):
    class Meta:
        model = IssueComment
        fields = ['comment', 'issue']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['issue'].widget = forms.HiddenInput()
