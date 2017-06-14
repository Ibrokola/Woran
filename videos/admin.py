from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Video, Category, TaggedItem





class TaggedItemInline(GenericTabularInline):
	model = TaggedItem


class VideoInline(admin.TabularInline):
	model = Video



class VideoAdmin(admin.ModelAdmin):
	inlines = [TaggedItemInline]
	list_display = ("__str__", 'slug')
	fields = ['title', 'order', 'share_message', 'embed_code', 'active', 'slug', 'featured', 'free_preview', 'category']
	# prepopulated_fields = {
	# 			'slug': ["title"],
	# }
	class Meta:
		model = Video


class CategoryAdmin(admin.ModelAdmin):
	inlines = [VideoInline, TaggedItemInline]
	class Meta:
		model = Category



admin.site.register(Video, VideoAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(TaggedItem)