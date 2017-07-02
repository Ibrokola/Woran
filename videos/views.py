from django.core.urlresolvers import reverse
from django.shortcuts import render, Http404, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.views.generic import (
		CreateView,
		DetailView,
		ListView,
		UpdateView,
		DeleteView
	)
from .models import Video
from categories.models import Category
from comments.models import Comment
from comments.forms import CommentForm
from analytics.signals import page_view
from .forms import VideoForm
from .mixins import MemberRequiredMixin, StaffMemberRequiredMixin



class VideoCreateView(StaffMemberRequiredMixin, CreateView):
	model = Video
	form_class = VideoForm
	# success_url = "/success/"

class VideoDetailView( MemberRequiredMixin, DetailView):
	queryset = Video.objects.all()

	# def get_object(self):
	# 	abc = self.kwargs.get('slug')
	# 	print(abc)
	# 	return get_object_or_404(Video, slug=abc)

	def get_context_data(self, *args, **kwargs):
		context = super(VideoDetailView, self).get_context_data(*args, **kwargs)
		return context




class VideoListView(ListView):
	# queryset = Video.objects.all()
	def get_queryset(self):
		request = self.request
		qs = Video.objects.all()
		query = request.GET.get('q')
		if query:
			qs = qs.filter(title__icontains=query)
		return qs

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(VideoListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context


class VideoUpdateView(StaffMemberRequiredMixin, UpdateView):
	queryset = Video.objects.all()
	form_class = VideoForm


class VideoDeleteView(StaffMemberRequiredMixin, DeleteView):
	queryset = Video.objects.all()
	success_url = '/videos/'




# @login_required

# def video_detail(request, cat_slug, vid_slug):
# 	cat = get_object_or_404(Category, slug=cat_slug)
# 	obj = get_object_or_404(Video, slug=vid_slug, category=cat)
# 	page_view.send(request.user, page_path=request.get_full_path(), primary_obj=obj, secondary_obj=cat)
# 	if request.user.is_authenticated() or obj.has_preview:
# 		try:
# 			is_member = request.user.is_member
# 		except:
# 			is_member = None
# 		if is_member or obj.has_preview:
# 			comments = obj.comment_set.all()
# 			for c in comments:
# 				c.get_children()
# 			template = "videos/video_detail.html"
# 			comment_form = CommentForm()
# 			context = {
# 				"obj": obj,
# 				"comments": comments,
# 				"comment_form": comment_form,
# 			}
# 			return render(request, template, context)
# 		else:
# 			# upgrade account
# 			next_url = obj.get_absolute_url()
# 			return HttpResponseRedirect("%s?next=%s"%(reverse('account_upgrade'), next_url))
# 	else:
# 		next_url = obj.get_absolute_url()
# 		return HttpResponseRedirect("%s?next=%s"%(reverse('account_login'), next_url))

		
		# return HttpResponseRedirect(next_url, 'account_login')  #A bit buggy
		# return HttpResponseRedirect(reverse('account_login'))


# def category_list(request):
# 	queryset = Category.objects.all()
# 	template = "videos/category_list.html"
# 	context = {
# 		"queryset":queryset
# 	}
# 	return render(request, template, context)

# @login_required
# def category_detail(request, cat_slug):
# 	obj = get_object_or_404(Category, slug=cat_slug)
# 	queryset = obj.video_set.all()
# 	page_view.send(request.user, page_path=request.get_full_path(), primary_obj=obj)
	
	# obj = Category.objects.get(slug=cat_slug) #Do not uncomment

	# context = {
	# 	"obj": obj,
	# 	"queryset":queryset,
	# }
	# template = "videos/video_list.html"
	# return render(request, template, context)



# def video_list(request):
# 	queryset = Video.objects.all()
# 	template = "videos/video_list.html"
# 	context = {
# 		"queryset":queryset
# 	}
# 	return render(request, template, context)