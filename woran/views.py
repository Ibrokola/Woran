from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.utils.safestring import mark_safe

from videos.models import Video


@login_required
def home(request):
	videos = Video.objects.all()
	template = 'home.html'
	video_embed = []

	for vid in videos:
		code = mark_safe(vid.embed_code)
		video_embed.append("%s" %(code))
	context = {
		"videos": videos,
		"number": videos.count(),
		"video_embed": video_embed,
		"a_code": mark_safe(videos[0].embed_code)
	}
	return render(request, template, context)






# def home(request):
# 	if request.user.is_authenticated():
# 		videos = Video.objects.all()
# 		template = 'home.html'
# 		video_embed = []

# 		for vid in videos:
# 			code = mark_safe(vid.embed_code)
# 			video_embed.append("%s" %(code))
# 		context = {
# 			"videos": videos,
# 			"number": videos.count(),
# 			"video_embed": video_embed,
# 			"a_code": mark_safe(videos[0].embed_code)
# 		}
# 		return render(request, template, context)
# 	else:
# 		return HttpResponseRedirect('accounts/login')


def login(request):
	template = 'home.html'
	context = {

	}
	return render(request, template, context)