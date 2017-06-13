import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, Http404, HttpResponseRedirect

from .models import Notification

@login_required
def all(request):
	notifications = Notification.objects.all_for_user(request.user)
	template = "notifications/all.html"
	context = {
			"notifications":notifications,
		}
	return render(request, template, context)

@login_required
def read(request, id):
	try:
		next = request.GET.get('next', None)
		notification = Notification.objects.get(id=id)
		if notification.recipient == request.user:
			notification.read = True
			notification.save()
			if next is not None:
				return HttpResponseRedirect(next)
			else:
				return HttpResponseRedirect(reverse("notifications_all"))
		else:
			raise Http404
	except:
		return HttpResponseRedirect(reverse("notifications_all"))

@login_required
def get_notifications_ajax(request):
	data = {
		"item1": "item 1",
		"item2": True,
	}
	print(data)
	json_data = json.dumps(data)
	print(json_data)
	return HttpResponse(json_data, content_type='application/json')