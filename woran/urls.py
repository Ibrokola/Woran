from django.conf.urls import url, include
from django.contrib import admin


from django.conf import settings
from django.conf.urls.static import static

# from django.views.generic import TemplateView home, video_detail, category_detail,

from .views import HomeView
# from videos.views import VideoListView, VideoDetailView, VideoCreateView, VideoUpdateView, VideoDeleteView
from comments.views import comment_thread, comment_create_view
from notifications.views import all, read, get_notifications_ajax
from billing.views import upgrade, billing_history, cancel_subscription
from django.views.generic import TemplateView
from accounts.views import account_home




urlpatterns = [
    url(r'^babs/admin/', admin.site.urls),
    url(r'^categories/', include('categories.urls', namespace='categories')),
    url(r'^series/', include('series.urls', namespace='series')),
    url(r'^videos/', include('videos.urls', namespace='videos')),

    # url(r'^home/$', TemplateView.as_view(template_name="home.html"), name='home'),

    url(r'^contact/$', TemplateView.as_view(template_name='company/contact_us.html'), name='contact_us'),
    # url(r'^$', home, name='home'),
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^videos/$', category_list, name='category_list'),
    # url(r'^videos/(?P<cat_slug>[\w-]+)/$', category_detail, name='category_detail'),
    
    # url(r'^videos/(?P<cat_slug>[\w-]+)/(?P<vid_slug>[\w-]+)/$', video_detail, name='video_detail'),
    
    url(r'^comment/create/$', comment_create_view, name='comment_create'),
    url(r'^comment/(?P<id>\d+)/$', comment_thread, name='comment_thread'),
    url(r'^notifications/$', all, name='notifications_all'),
    url(r'^notifications/ajax/$', get_notifications_ajax, name='get_notifications_ajax'),
    url(r'^notifications/read/(?P<id>\d+)/$', read, name='notifications_read'),
    url(r'^upgrade/$', upgrade, name='account_upgrade'),
    url(r'^billing/$', billing_history, name='billing_history'),
    url(r'^billing/cancel$', cancel_subscription, name='cancel_subscription'),
    url(r'^account/$', account_home, name='account_home'),
    url(r'^accounts/', include('allauth.urls')),
]




if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)