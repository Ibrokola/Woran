from django.contrib import admin

from .forms import CategoryAdminForm
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
	# inlines = [TaggedItemInline]
	list_filter = ['updated', 'timestamp']
	list_display = ["title", 'updated', 'timestamp']
	readonly_fields = ['updated', 'timestamp']
	# fields = ['title', 'slug', 'order', 'video', 'description', 'active', 'featured', 'timestamp', 'updated']
	search_fields = ['title']
	form = CategoryAdminForm

	# class Meta:
	# 	model = Category

admin.site.register(Category, CategoryAdmin)