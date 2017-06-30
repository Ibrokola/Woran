from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.db.models import Prefetch
from series.utils import create_slug

from series.fields import PositionField





class CategoryQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

	def featured(self):
		return self.filter(featured=True)



class CategoryManager(models.Manager):
	def get_queryset(self):
		return CategoryQuerySet(self.model, using=self._db)

	def get_featured(self):
		# return super(VideoManager, self).filter(featured=True)
		return self.get_queryset().active().featured()

	def all(self):
		return self.get_queryset().all().active().prefetch_related('primary_category')
		



class Category(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True, blank=True)
	order = PositionField(blank=True)
	description = models.TextField(max_length=5000, null=True, blank=True)
	# tags = GenericRelation("TaggedItem", null=True, blank=True)
	# image = models.ImageField(upload_to='images/', null=True, blank=True)
	active = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	objects = CategoryManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		# return "/videos/{slug_arg}/".format(slug_arg=self.slug)
		return reverse('categories:detail', kwargs={"slug": self.slug})


def category_pre_save_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(category_pre_save_reciever, sender=Category)