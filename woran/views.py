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

	signup_form = SignupForm(request.POST or None)
	if signup_form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password2']
		# MyUser.objects.create_user(username=username, email=email, password=password)
		new_user = MyUser()
		new_user.username = username
		new_user.email = email
		new_user.set_password(password)
		new_user.save()
		return redirect('account_login')

	# login_form = LoginForm()
	# form = RegisterForm()
	# videos = Video.objects.all()
	template = 'home.html'
	# video_embed = []

	# for vid in videos:
	# 	code = mark_safe(vid.embed_code)
	# 	video_embed.append("%s" %(code))
	context = {
		# "videos": videos,
		# "number": videos.count(),
		# "video_embed": video_embed,
		# "a_code": mark_safe(videos[0].embed_code),
		"form": signup_form,
		# "login_form": login_form,
		# "form": form,
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