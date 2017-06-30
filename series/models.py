from django.conf import settings
from django.db import models
from django.db.models import Prefetch
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_save

from django.utils.text import slugify
from .utils import create_slug

from categories.models import Category
from videos.models import Video
from .fields import PositionField




class MySeries(models.Model):
	# user      = models.OneToOneField(settings.AUTH_USER_MODEL)
	user      = models.ForeignKey(settings.AUTH_USER_MODEL)
	series 	  = models.ManyToManyField('Series', related_name='watched', blank=True)
	updated   = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.series.all().count())

	class Meta:
		verbose_name = 'My series'
		verbose_name_plural = 'My series'

def post_save_user_create(sender, instance, created, *args, **kwargs):
	if created:
		MyCourses.objects.get_or_create(user=instance)

post_save.connect(post_save_user_create, sender=settings.AUTH_USER_MODEL)


DEFAULT_MESSAGE = 'Check out this African Series'

# POS_CHOICES = (
# 		('main', 'Main'),
# 		('sec', 'Secondary'),
# 	)


class SeriesQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

	def watched(self, user):
		return self.prefetch_related(
					Prefetch('watched',
							queryset=MySeries.objects.filter(user=user),
							to_attr='is_watcher'
					)
				)

class SeriesManager(models.Manager):
	def get_queryset(self):
		return SeriesQuerySet(self.model, using=self._db)

	def all(self):
		return self.get_queryset().all().active()
		# return super(SeriesManager, self).all()



class Series(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(blank=True, null=True)
	# category = models.CharField(max_length=120, choices=POS_CHOICES, default='main')
	category      = models.ForeignKey(Category, related_name='primary_category', null=True, blank=True)
	order = PositionField(collection='category')
	share_message = models.CharField(max_length=250, default=DEFAULT_MESSAGE)
	description = models.TextField()
	active = models.BooleanField(default=True)
	# featured = models.BooleanField(default=False)
	# free_preview = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) #time added
	updated = models.DateTimeField(auto_now_add=False, auto_now=True) #last saved

	objects = SeriesManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("series:detail", kwargs={"slug": self.slug})



class Episode(models.Model):
	series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True)
	video = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=120)
	order = PositionField(collection='series')
	# order = models.IntegerField()
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
		ordering = ['order', 'title'] #0-100, a-z

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