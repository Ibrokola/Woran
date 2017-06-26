from django.conf.urls import url 

from .views import (
		SeriesListView,
		SeriesDetailView,
		SeriesCreateView,
		SeriesUpdateView,
		SeriesDeleteView,
		EpisodeDetailView
	)

urlpatterns = [
	url(r'^$', SeriesListView.as_view(), name='list'),
	url(r'^create/$', SeriesCreateView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', SeriesDetailView.as_view(), name='detail'),
	url(r'^(?P<se_slug>[\w-]+)/(?P<ep_slug>[\w-]+)/$', EpisodeDetailView.as_view(), name='episode_detail'),
	url(r'^(?P<slug>[\w-]+)/edit/$', SeriesUpdateView.as_view(), name='update'),
	url(r'^(?P<slug>[\w-]+)/delete/$', SeriesDeleteView.as_view(), name='delete'),
]