from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
from .utils import create_slug

from videos.models import Video

DEFAULT_MESSAGE = 'Check out this African Series'

class Series(models.Model):
	title = models.CharField(max_length=120)
	share_message = models.TextField(default=DEFAULT_MESSAGE)
	description = models.TextField()
	# active = models.BooleanField(default=True)
	# featured = models.BooleanField(default=False)
	slug = models.SlugField(blank=True, null=True)
	# free_preview = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) #time added
	updated = models.DateTimeField(auto_now_add=False, auto_now=True) #last saved


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("series:detail", kwargs={"slug": self.slug})



class Episode(models.Model):
	series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True)
	video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=120)
	slug = models.SlugField(blank=True, null=True)
	share_message = models.TextField(default=DEFAULT_MESSAGE)
	description = models.TextField(blank=True)
	# active = models.BooleanField(default=True)
	# featured = models.BooleanField(default=False)
	# free_preview = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) #time added
	updated = models.DateTimeField(auto_now_add=False, auto_now=True) #last saved


	def __str__(self):
		return self.title

	class Meta:
		unique_together = (('slug', 'series'),)

	def get_absolute_url(self):
		return reverse("series:episode_detail",
				kwargs={
					"se_slug": self.series.slug,
					"ep_slug": self.slug
				}
			)



def video_pre_save_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(video_pre_save_reciever, sender=Series)
# pre_save.connect(video_pre_save_reciever, sender=Episode)