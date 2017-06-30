from django.conf.urls import url 

from .views import (
	CategoryListView,
	CategoryDetailView,
	)

urlpatterns = [
	
	url(r'^$', CategoryListView.as_view(), name='list'),
	# url(r'^videos/(?P<pk>\d+)/$', VideoDetailView.as_view(), name='video_detail'),
    url(r'^(?P<slug>[\w-]+)/$', CategoryDetailView.as_view(), name='detail'),
]