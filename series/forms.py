from django import forms

from videos.models import Video
from .models import Series, Episode



class EpisodeAdminForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = [
            'order',
            'video',
            'title',
            'slug',
            'description',
            'share_message'
        ]

    def __init__(self, *args, **kwargs):
        super(EpisodeAdminForm, self).__init__(*args, **kwargs)
        obj = kwargs.get("instance")
        qs = Video.objects.filter(episode__isnull=True)
        if obj:
            if obj.video:
                this_ = Video.objects.filter(pk=obj.video.pk)
                qs = (qs | this_)
            self.fields['video'].queryset = qs
        else:
            self.fields['video'].queryset = qs




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