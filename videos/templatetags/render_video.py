from django import template


register = template.Library()

from videos.models import Video

@register.inclusion_tag('videos/snippets/render_video.html')
def render_video(video_obj):
	video = None
	if isinstance(video_obj, Video):
		video = video_obj.embed_code
	# qs = Video.objects.filter(id=video_id)
	# if qs.exists():
	# 	video = qs.first().embed_code
	return {'video': video}








# @register.inclusion_tag('home.html')
# def signup_form_tag(current_page=None):
#     return {'signupform': SignupForm(),
#             'redirect_to': current_page}