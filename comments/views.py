from django.shortcuts import render

from .models import Comment
from .forms import CommentForm

def comment_thread(request, id):
	comment = Comment.objects.get(id=id)
	form = CommentForm(request.POST or None)
	context = {
		"form": form,
		"comment":comment,
	}
	template = "comments/comment_thread.html"
	return render(request, template, context)