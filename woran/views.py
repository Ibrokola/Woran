from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe
from django.views.generic import View

from allauth.account.views import *
from allauth.account.forms import *  
# from accounts.forms import RegisterForm

from videos.models import Video
from accounts.models import MyUser
from comments.models import Comment
from analytics.signals import page_view

# from analytics.models import PageView
from videos.models import Video
from categories.models import Category 
from django.db.models import Count 


			###############
			###############
			## Home Page ##
			###############
			###############

			
class HomeView(View):
	def get(self, request, *args, **kwargs):
		# page_view.send(
		# request.user,
		# page_path=request.get_full_path()
		# )
		if request.user.is_authenticated():
			# page_view_objs = request.user.pageview_set.get_videos()[:6]
			# recent_videos = []
			# for obj in page_view_objs:
			# 	if not obj.primary_object in recent_videos:
			# 		recent_videos.append(obj.primary_object)
			recent_comments = Comment.objects.recent()

			video_type = ContentType.objects.get_for_model(Video)
			# popular_videos_list = PageView.objects.filter(primary_content_type=video_type).values("primary_object_id").annotate(the_count=Count("primary_object_id")).order_by("-the_count")[:2]

			# popular_videos = []
			# for item in popular_videos_list:
			# 	try:
			# 		new_video = Video.objects.get(id=item['primary_object_id'])
			# 		popular_videos.append(new_video)
			# 	except:
			# 		pass

			# PageView.objects.filter(primary_content_type=video_type, primary_object_id=5).count()


			context = {
				# "popular_videos":popular_videos,
				# "recent_videos":recent_videos,
				"recent_comments":recent_comments
				}
			template = 'home_logged_in.html'
		else:
			# featured_categories = Category.objects.get_featured()
			featured_videos = Video.objects.get_featured()
			signup_form = SignupForm()
			login_form = LoginForm()
			template = 'home_visitor.html'
			context = {
				"signup_form": signup_form,
				"login_form":login_form,
				# "featured_categories": featured_categories,
				"featured_videos": featured_videos
			}
		return render(request, template, context)



# @login_required
# def home(request):
# 	page_view.send(
# 		request.user,
# 		page_path=request.get_full_path()
# 	)
# 	if request.user.is_authenticated():
# 		page_view_objs = request.user.pageview_set.get_videos()[:6]
# 		recent_videos = []
# 		for obj in page_view_objs:
# 			if not obj.primary_object in recent_videos:
# 				recent_videos.append(obj.primary_object)
# 		recent_comments = Comment.objects.recent()

# 		video_type = ContentType.objects.get_for_model(Video)
# 		popular_videos_list = PageView.objects.filter(primary_content_type=video_type).values("primary_object_id").annotate(the_count=Count("primary_object_id")).order_by("-the_count")[:2]

# 		popular_videos = []
# 		for item in popular_videos_list:
# 			try:
# 				new_video = Video.objects.get(id=item['primary_object_id'])
# 				popular_videos.append(new_video)
# 			except:
# 				pass

# 		PageView.objects.filter(primary_content_type=video_type, primary_object_id=5).count()


# 		context = {
# 			"popular_videos":popular_videos,
# 			"recent_videos":recent_videos,
# 			"recent_comments":recent_comments
# 			}
# 		template = 'home_logged_in.html'
# 	else:
# 		featured_categories = Category.objects.get_featured()
# 		featured_videos = Video.objects.get_featured()
# 		signup_form = SignupForm()
# 		login_form = LoginForm()
# 		template = 'home_visitor.html'
# 		context = {
# 			"signup_form": signup_form,
# 			"login_form":login_form,
# 			"featured_categories": featured_categories,
# 			"featured_videos": featured_videos
# 		}
# 	return render(request, template, context)






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


# def login(request):
# 	template = 'home.html'
# 	context = {

# 	}
# 	return render(request, template, context)