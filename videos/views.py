from django.shortcuts import render, Http404
from django.contrib.auth.decorators import login_required

from .models import Video, Category


@login_required
def video_detail(request, cat_slug, id):
	try:
		cat = Category.objects.get(slug=cat_slug)
	except:
		raise Http404
	try:
		obj = Video.objects.get(id=id)
		template = "videos/video_detail.html"
		context = {
			"obj": obj,
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