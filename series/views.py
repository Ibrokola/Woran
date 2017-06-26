from django.shortcuts import render, get_object_or_404

# from .forms import VideoForm
from django.http import Http404
from videos.mixins import MemberRequiredMixin, StaffMemberRequiredMixin
from django.views.generic import (
		CreateView,
		DetailView,
		ListView,
		UpdateView,
		DeleteView
	)
from .models import Series, Episode
from .forms import SeriesForm

class SeriesCreateView(StaffMemberRequiredMixin, CreateView):
	model = Series
	form_class = SeriesForm


	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return super(SeriesCreateView, self).form_valid(form)

class EpisodeDetailView(MemberRequiredMixin, DetailView):
	def get_object(self):
		series_slug = self.kwargs.get("se_slug")
		episode_slug = self.kwargs.get("ep_slug")
		obj = get_object_or_404(Episode, series__slug=series_slug, slug=episode_slug)
		return obj 






# detail view for the video series
class SeriesDetailView(MemberRequiredMixin, DetailView):
	queryset = Series.objects.all()

	# def get_object(self):
	# 	abc = self.kwargs.get('slug')
	# 	print(abc)
	# 	return get_object_or_404(Video, slug=abc)

	def get_object(self):
		slug = self.kwargs.get('slug') #slug definition
		# obj = Series.objects.get(slug=slug) # returns MultipleObjectsReturned error, don't do this
		obj = Series.objects.filter(slug=slug) #returns a list of objects
		if obj.exists():
			return obj.first() # returns first instance of that list...
		raise Http404

		# or

		# try:
		# 	obj = Series.objects.get(slug=slug)
		# except Series.MultipleObjectsReturned:     But seriously don't do this
		# 	qs = Series.objects.filter(slug=slug)
		# 	if qs.exists():
		# 		obj = qs.frist()
		# except:
		# 	raise Http404
		# return obj 

	def get_context_data(self, *args, **kwargs):
		context = super(SeriesDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context




class SeriesListView(ListView):
	# queryset = Video.objects.all()
	def get_queryset(self):
		request = self.request
		qs = Series.objects.all()
		query = request.GET.get('q')
		if query:
			qs = qs.filter(title__icontains=query)
		return qs

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(VideoListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context


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
