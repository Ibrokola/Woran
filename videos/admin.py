from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Video





# class TaggedItemInline(GenericTabularInline):
# 	model = TaggedItem


class VideoInline(admin.TabularInline):
	model = Video



class VideoAdmin(admin.ModelAdmin):
	# inlines = [TaggedItemInline]
	list_filter = ['updated', 'timestamp']
	list_display = ["title", 'updated', 'timestamp']
	readonly_fields = ['updated', 'timestamp']
	fields = ['title', 'slug', 'order', 'share_message', 'embed_code', 'active', 'featured', 'free_preview']
	search_fields = ['title']

	class Meta:
		model = Video


# class CategoryAdmin(admin.ModelAdmin):
# 	inlines = [VideoInline]
# 	class Meta:
# 		model = Category



admin.site.register(Video, VideoAdmin)
# admin.site.register(Category, CategoryAdmin)

# admin.site.register(TaggedItem)