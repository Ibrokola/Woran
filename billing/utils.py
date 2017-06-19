import datetime
from django.utils import timezone

from decouple import config

import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id=config("merchant_id"),
                                  public_key=config("public_key"),
                                  private_key=config("private_key"))


from .signals import membership_dates_update

def check_membership_status(subscription_id):
	sub = braintree.Subscription.find(subscription_id)
	if sub.status == "Active":
		status = True
		nex_billing_date = sub.next_billing_date
	else:
		status = False
		next_billing_date = None
	return status, next_billing_date


def update_braintree_membership(user):
	user = user
	membership = user.membership
	now = timezone.now()
	subscription_id = user.usermerchantid.subscription_id
	if membership.date_end <= timezone.now() and subscription_id is not None:
		status, next_billing_date = check_membership_status(subscription_id)
		
		if status:
			small_time = datetime.time(0,0,0,1)
			datetime_obj = datetime.datetime.combine(next_billing_date, small_time)
			datetime_aware = timezone.make_aware(datetime_obj, timezone.get_current_timezone())
			membership_dates_update.send(membership, new_date_start=datetime_aware)
		else:
			membership.update_status()
	elif subscription_id is None:
		membership.update_status()
	else:
		pass