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
	print(queryset)

class CategoryDetailView(DetailView):
	queryset = Category.objects.all()
	print(queryset)
