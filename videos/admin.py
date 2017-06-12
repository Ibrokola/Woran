from django.contrib import admin


from .models import Video, Category


class VideoAdmin(admin.ModelAdmin):
	list_display = ("__str__", 'slug')
	fields = ['title', 'share_message', 'embed_code', 'active', 'slug', 'featured', 'free_preview', 'category']
	# prepopulated_fields = {
	# 			'slug': ["title"],
	# }
	class Meta:
		model = Video


admin.site.register(Video, VideoAdmin)
admin.site.register(Category)