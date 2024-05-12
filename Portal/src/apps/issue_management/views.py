from django.shortcuts import render
from django.shortcuts import redirect
from apps.issue_management.models import(
    Issue,
    IssueComment
)
from apps.issue_management.forms import(
    IssueForm,
    CommentForm
)

# class MainView(TemplateView):
#     issues = Issue.objects.all()
#     template_name = 'issue_management/main.html'

def main(request):
    if request.method=="POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
    form = IssueForm()
    issues = Issue.objects.all()
    context = {"issues":issues, "form":form}
    return render(request, "issue_management/main.html", context=context)

def detail(request, issue_id):
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()

    issue = Issue.objects.get(id=issue_id)
    form = CommentForm(initial={
        "issue" : issue
    })
    return render(request, "issue_management/detail.html", context={"issue":issue,"comment_form":form})


def update_issue(request):
    redirect("issue_main")

def delete_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    issue.delete()
    return redirect("issue_main")

def update_comment():
    pass

def delete_issue_comment(request, issue_comment_id):
    issue_comment = IssueComment.objects.get(id=issue_comment_id)
    issue_id = issue_comment.issue.id
    issue_comment.delete()
    return redirect("issue_detail", issue_id)

def post_comment(request, issue_id, comment):
    if request.method=="POST":
        issue_comment = IssueComment()
        issue_comment.comment = comment
        issue_comment.issue = Issue.objects.get(id=issue_id)