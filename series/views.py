import random
from django.shortcuts import render, get_object_or_404

# from .forms import VideoForm
from django.db.models import Prefetch
from django.http import Http404
from videos.mixins import MemberRequiredMixin, StaffMemberRequiredMixin
from django.views.generic import (
		CreateView,
		DetailView,
		ListView,
		UpdateView,
		DeleteView,
		View
	)
from .models import Series, Episode, MySeries
from .forms import SeriesForm

class SeriesCreateView(StaffMemberRequiredMixin, CreateView):
	model = Series
	form_class = SeriesForm


	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return super(SeriesCreateView, self).form_valid(form)


class EpisodeDetailView(View):
	def get(self, request, se_slug=None, ep_slug=None, *args, **kwargs):
		obj = None
		qs = Series.objects.filter(slug=se_slug).episodes()
		series_ = qs.first()
		episodes_qs = series_.episode_set.filter(slug=ep_slug)
		obj = episodes_qs.first()

		if request.user.is_authenticated() or obj.has_preview:
			try:
				is_member = request.user.is_member
			except:
				is_member = None
			if is_member or obj.has_preview:
				template = "series/episode_detail.html"
				context = {
					"object": obj,
					"series": series_,
				}
				return render(request, template, context)
			else:
				# upgrade account
				next_url = obj.get_absolute_url()
				return HttpResponseRedirect("%s?next=%s"%(reverse('account_upgrade'), next_url))
		else:
			next_url = obj.get_absolute_url()
			return HttpResponseRedirect("%s?next=%s"%(reverse('account_login'), next_url))


		# def get_object(self):
		# 	series_slug = self.kwargs.get("se_slug")
		# 	episode_slug = self.kwargs.get("ep_slug")
		# 	obj = get_object_or_404(Episode, series__slug=series_slug, slug=episode_slug)
		# 	return obj 




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






# detail view for the video series
class SeriesDetailView(MemberRequiredMixin, DetailView):
	def get_object(self):
		slug = self.kwargs.get('slug') #slug definition
		# obj = Series.objects.get(slug=slug) # returns MultipleObjectsReturned error, don't do this
		obj = Series.objects.filter(slug=slug).watched(self.request.user) #returns a list of watched objects
		if obj.exists():
			return obj.first() # returns first instance of that list...
		raise Http404

	def get_context_data(self, *args, **kwargs):
		context = super(SeriesDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context




class SeriesListView(ListView):
	# queryset = Video.objects.all()
	paginate_by = 12

	def get_context_data(self, *args, **kwargs):
		context = super(SeriesListView, self).get_context_data(*args, **kwargs)
		# print(dir(context.get('page_obj')))
		return context

	def get_queryset(self):
		request = self.request
		qs = Series.objects.all()
		query = request.GET.get('q')
		user = self.request.user
		if query:
			qs = qs.filter(title__icontains=query)
		if user.is_authenticated():
			qs = qs.watched(user)
		return qs



class SeriesUpdateView(StaffMemberRequiredMixin, UpdateView):
	queryset = Series.objects.all()
	form_class = SeriesForm

	def form_valid(self, form):
		obj = form.save(commit=False)
		if not request.user.is_staff:
			obj.user = self.request.user
		obj.save()
		return super(SeriesUpdateView, self).form_valid(form)


	def get_object(self):
		slug = self.kwargs.get('slug') #slug definition
		# obj = Series.objects.get(slug=slug) # returns MultipleObjectsReturned error, don't do this
		obj = Series.objects.filter(slug=slug) #returns a list of objects
		if obj.exists():
			return obj.first() # returns first instance of that list...
		raise Http404



class SeriesDeleteView(StaffMemberRequiredMixin, DeleteView):
	queryset = Series.objects.all()
	success_url = '/series/'


	def get_object(self):
		slug = self.kwargs.get('slug') #slug definition
		# obj = Series.objects.get(slug=slug) # returns MultipleObjectsReturned error, don't do this
		obj = Series.objects.filter(slug=slug) #returns a list of objects
		if obj.exists():
			return obj.first() # returns first instance of that list...
		raise Http404
