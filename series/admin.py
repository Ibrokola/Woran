from django.contrib import admin

from .models import Series, Episode

class EpisodeInline(admin.TabularInline):
	model = Episode
	prepopulated_fields = {"slug": ("title", )}
	




class SeriesAdmin(admin.ModelAdmin):
	inlines = [EpisodeInline]
	list_filter = ['updated', 'timestamp']
	list_display = ["title", 'updated', 'timestamp']
	readonly_fields = ['updated', 'timestamp']
	search_fields = ['title', 'description']


	class Meta:
		models = Series

admin.site.register(Series, SeriesAdmin)