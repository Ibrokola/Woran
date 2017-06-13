from django.shortcuts import render, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .models import Video, Category, TaggedItem
from comments.models import Comment
from comments.forms import CommentForm

@login_required
def video_detail(request, cat_slug, vid_slug):
	obj = Video.objects.get(slug=vid_slug)
	comments = obj.comment_set.all()
	# content_type = ContentType.objects.get_for_model(obj)
	# tags = TaggedItem.objects.filter(content_type=content_type, object_id=obj.id)
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
		comment_form = CommentForm()
		context = {
			"obj": obj,
			"comments": comments,
			"comment_form": comment_form,
		}
		return render(request, template, context)
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