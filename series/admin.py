from django.contrib import admin
from .forms import EpisodeAdminForm
from .models import Series, Episode, MySeries




class EpisodeInline(admin.TabularInline):
	model = Episode
	form = EpisodeAdminForm
	prepopulated_fields = {"slug": ("title", )}
	extra = 1
	# raw_id_fields = ['video']
	




class SeriesAdmin(admin.ModelAdmin):
	inlines = [EpisodeInline]
	list_filter = ['updated', 'timestamp']
	list_display = ["title", 'updated', 'timestamp', 'order']
	readonly_fields = ['updated', 'timestamp']
	search_fields = ['title', 'description']
	list_editable = ['order']


	class Meta:
		models = Series

admin.site.register(Series, SeriesAdmin)
admin.site.register(MySeries)