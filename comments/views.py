from django.shortcuts import render, Http404, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from notifications.signals import notify
from videos.models import Video
from .models import Comment
from .forms import CommentForm

@login_required
def comment_thread(request, id):
	comment = get_object_or_404(Comment, id=id)
	form = CommentForm()
	context = {
		"form": form,
		"comment":comment,
	}
	template = "comments/comment_thread.html"
	return render(request, template, context)

@login_required
def comment_create_view(request):
	if request.method == "POST" and request.user.is_authenticated():
		parent_id = request.POST.get('parent_id')
		video_id = request.POST.get('video_id')
		origin_path = request.POST.get('origin_path')
		try:
			video = Video.objects.get(id=video_id)
		except:
			video = None
		parent_comment = None
		if parent_id is not None:
			try:
				parent_comment = Comment.objects.get(id=parent_id)
			except:
				parent_comment = None

			if parent_comment is not None and parent_comment.video is not None:
				video = parent_comment.video

		form = CommentForm(request.POST)
		if form.is_valid():
			comment_text = form.cleaned_data['comment']
			if parent_comment is not None:
				new_comment = Comment.objects.create_comment(
						user=request.user,
						path=parent_comment.get_origin,
						text=comment_text,
						video=video,
						parent=parent_comment,
					)
				affected_users = parent_comment.get_affected_users()
				notify.send(
						request.user,
						action=new_comment, 
						target=parent_comment, 
						recipient=parent_comment.user,
						affected_users=affected_users, 
						verb='replied to'
					)
				messages.success(request, "Thanks for your response")
				return HttpResponseRedirect(parent_comment.get_absolute_url())
			else:
				new_comment = Comment.objects.create_comment(
						user=request.user,
						path=origin_path,
						text=comment_text,
						video=video,
					)
				#option to send to super user or staff users
				# notify.send(
				# 		request.user, 
				# 		recipient=request.user, 
				# 		action=new_comment,
				# 		target=new_comment.video,
				# 		verb='commented on'
				# 	)
				# notify.send(request.user, recipient=request.user, verb='New comment added')
				messages.success(request, "Thanks for your comment")
				return HttpResponseRedirect(new_comment.get_absolute_url())
		else:
			message.error(request, "There was an error with your comment.")
			return HttpResponseRedirect(origin_path)

			# 	new_comment = Comment.objects.create_comment(
			# 			user=request.user,
			# 			path=parent_comment.get_origin,
			# 			text=comment_text,
			# 			video=obj,
			# 			parent=parent_comment,			# 		)

	else:
		raise Http404