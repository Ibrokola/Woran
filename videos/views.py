from django.shortcuts import render, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Video, Category
from comments.models import Comment
from comments.forms import CommentForm

@login_required
def video_detail(request, cat_slug, vid_slug):
	obj = Video.objects.get(slug=vid_slug)
	comments = obj.comment_set.all()
	for c in comments:
		c.get_children()
	try:
		cat = Category.objects.get(slug=cat_slug)
	except:
		raise Http404
	try:
		obj = Video.objects.get(slug=vid_slug)
		comments = obj.comment_set.all()
		# comments = Comment.objects.filter(video=obj)
		template = "videos/video_detail.html"
		comment_form = CommentForm(request.POST or None)
		context = {
			"obj": obj,
			"comments": comments,
			# "comment_form": comment_form,
		}
		if comment_form.is_valid():
			parent_id = request.POST.get('parent_id')
			parent_comment = None
			if parent_id is not None:
				try:
					parent_comment = Comment.objects.get(id=parent_id)
				except:
					parent_comment = None


			comment_text = comment_form.cleaned_data['comment']
			new_comment = Comment.objects.create_comment(
						user=request.user,
						path=request.get_full_path(),
						text=comment_text,
						video=obj,
						parent=parent_comment,
					)
			# print(new_comment.text)
			return HttpResponseRedirect(obj.get_absolute_url())
			# return render(request, template, context)
		
		return render(request, template, {"obj": obj, "comments": comments, "comment_form": comment_form})
	except:
		raise Http404


def category_list(request):
	queryset = Category.objects.all()
	template = "videos/category_list.html"
	context = {
		"queryset":queryset
	}
	return render(request, template, context)

@login_required
def category_detail(request, cat_slug):
	path = request.get_full_path()
	try:
		obj = Category.objects.get(slug=cat_slug)
		queryset = obj.video_set.all()
		context = {
			"obj": obj,
			"queryset":queryset,
		}
		template = "videos/video_list.html"
		return render(request, template, context)
	except:
		raise Http404


# def video_list(request):
# 	queryset = Video.objects.all()
# 	template = "videos/video_list.html"
# 	context = {
# 		"queryset":queryset
# 	}
# 	return render(request, template, context)