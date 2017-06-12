from django.conf.urls import url, include
from django.contrib import admin


from django.conf import settings
from django.conf.urls.static import static

# from django.views.generic import TemplateView

from .views import home
from videos.views import video_detail, category_list, category_detail





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^home/$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^$', home, name='home'),
    url(r'^videos/$', category_list, name='category_list'),
    url(r'^videos/(?P<cat_slug>[\w-]+)/$', category_detail, name='category_detail'),
    url(r'^videos/(?P<cat_slug>[\w-]+)/(?P<vid_slug>[\w-]+)/$', video_detail, name='video_detail'),
    url(r'^accounts/', include('allauth.urls')),
]




if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)