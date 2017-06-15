import random
from django.shortcuts import render

from .models import Transaction, Membership
from .signals import membership_dates_update

import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="use_your_merchant_id",
                                  public_key="use_your_public_key",
                                  private_key="use_your_private_key")



def upgrade(request):
	if request.user.is_authenticated():
		trans = Transaction.objects.create_new(request.user, "anbnehrg%s"%(random.randint(0,100)), 25.00, "visa")
		if trans.success:	
			membership_instance, created = Membership.objects.get_or_create(user=request.user)
			membership_dates_update.send(membership_instance, new_date_start=trans.timestamp)
		template = "billing/upgrade.html"
		context = {}
	return render(request, template, context)


def billing_history(request):
	history = Transaction.objects.filter(user=request.user, success=True)
	context = {"queryset": history}
	template = "billing/history.html"
	return render(request, template, context)