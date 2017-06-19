from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from billing.models import Transaction
from notifications.models import Notification





@login_required
def account_home(request):
	notifications = Notification.objects.get_recent_for_user(request.user, 3)
	transactions = Transaction.objects.get_recent_for_user(request.user, 3)
	context = {
		"notifications": notifications,
		"transactions": transactions
	}
	return render(request, "account_home.html", context)