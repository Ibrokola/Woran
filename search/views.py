from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View

from categories.models import Category
from series.models import Series, Episode



class SearchView(View):
	def get(self, request, *args, **kwargs):
		template = "search/default.html"
		query = request.GET.get('q')
		qs = None
		c_qs = None
		e_qs = None
		if query:
			ep_lookup = Q(title__icontains=query) \
			| Q(description__icontains=query)

			query_lookup = ep_lookup | Q(category__title__icontains=query)\
			| Q(category__description__icontains=query)\
			| Q(episode__title__icontains=query)
			
			qs = Series.objects.all().episodes().filter(
						query_lookup
					).distinct()
			qs_ids = [x.id for x in qs]

			cat_lookup = Q(primary_category__in=qs_ids) | Q(secondary_category__in=qs_ids)
			c_qs = Category.objects.filter(ep_lookup | cat_lookup).distinct()
			e_qs = Episode.objects.filter(ep_lookup).distinct()

		context = { "qs":qs, "c_qs":c_qs, "e_qs":e_qs } 
		return render(request, template, context)