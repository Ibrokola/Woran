from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.utils.safestring import mark_safe
from allauth.account.views import *
from allauth.account.forms import *  
# from accounts.forms import RegisterForm

from videos.models import Video
from accounts.models import MyUser




# @login_required
def home(request):
	if request.user.is_authenticated():
		context = {}
	else:
		signup_form = SignupForm()
		login_form = LoginForm()
		# template = 'home.html'
		context = {
			"signup_form": signup_form,
			"login_form":login_form,
		}
	return render(request, 'home.html', context)






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