from django.shortcuts import render

from .models import Category
from django.views.generic import (
		CreateView,
		DetailView,
		ListView,
		UpdateView,
		DeleteView
	)

class CategoryListView(ListView):
	queryset = Category.objects.all().order_by('title')


class CategoryDetailView(DetailView):
	queryset = Category.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
		# obj = self.get_object()
		obj = context.get("object")
		user = self.request.user
		qs1 = obj.primary_category.all().watched(self.request.user)
		context['featured_series'] = qs1[:6]
		qs2 = obj.secondary_category.all().watched(self.request.user)
		# if user.is_authenticated():	
		# 	qs1 = qs1.watched(self.request.user)
		# 	qs2 = qs2.watched(self.request.user)
		qs = (qs1 | qs2).distinct()
		context['series'] = qs
		return context 
	
