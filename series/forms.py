from django import forms

from .models import Series



class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = [
        	'title',
        	'description',
        	# 'free_preview',
        ] 

    def clean_slug(self):
    	slug = self.cleaned_data.get("slug")
    	qs = Series.objects.filter(slug=slug)
    	if qs.counts() > 1:
    		raise forms.ValidationError("Series must be unique")
    	return slug 