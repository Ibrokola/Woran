from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, Http404

from django.utils import timezone

from .models import Transaction, Membership, UserMerchantId
from .signals import membership_dates_update

from decouple import config

import random

import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id=config("merchant_id"),
                                  public_key=config("public_key"),
                                  private_key=config("private_key"))

PLAN_ID = "monthly"



def get_or_create_model_transaction(user, braintree_transaction):
	trans_id = braintree_transaction.id
	try:
		trans = Transaction.objects.get(user=user, tansaction_id=trans_id)
		created = False
	except:
		created = True
		payment_type = braintree_transaction.payment_instrument_type	
		amount = braintree_transaction.amount
		if payment_type == braintree.PaymentInstrumentType.PayPalAccount:
			trans = Transaction.objects.create_new(user, trans_id, amount, "PayPal")
			# trans_success = trans.success
			# trans_timestamp = trans.timestamp
		elif payment_type == braintree.PaymentInstrumentType.CreditCard:
			credit_card_details = braintree_transaction.credit_card_details
			card_type = credit_card_details.card_type
			last_4 = credit_card_details.last_4
			trans = Transaction.objects.create_new(user, trans_id, amount, card_type, last_four = last_4)
			# trans_success = trans.success
			# trans_timestamp = trans.timestamp
		else:
			created = False
			trans = None
			# trans_success = False
	return trans, created



# @login_required
def update_transactions(user):
	bt_transactions = braintree.Transaction.search(
				braintree.TransactionSearch.customer_id == user.usermerchantid.customer_id
			)
	try:
		django_transactions = user.transaction_set.all()
	except:
		django_transactions = None

	if bt_transactions is not None and django_transactions is not None:
		if bt_transactions.maximum_size <= django_transactions.count():
			pass
		else:
			for bt_tran in bt_transactions.items:
				new_tran, created = get_or_create_model_transaction(user, bt_tran)




@login_required
def cancel_subscription(request):
	sub_id = request.user.usermerchantid.subscription_id
	if sub_id:
		result = braintree.Subscription.cancel(sub_id)
		if result.is_success:
			request.user.usermerchantid.subscription_id = None
			request.user.usermerchantid.save()
			messages.success(request, "Your subscription has been successfully deactivated")
		else:
			messages.error(request, "There was an error deactiavting your subscription, please contact us.")
	else:
		messages.success(request, "You do not have an active subscription")	
	return redirect('account_home')

@login_required
def billing_history(request):	
	update_transactions(request.user)
		# pass
	history = Transaction.objects.filter(user=request.user).filter(success=True)
	context = {"queryset": history}
	template = "billing/history.html"
	return render(request, template, context)




def upgrade(request):
	if request.user.is_authenticated():
		try:
			merchant_obj = UserMerchantId.objects.get(user=request.user)
		except:
			messages.error(request, "There was an error with your account. Please contact us.")
			return redirect("contact_us")

		
		merchant_customer_id = merchant_obj.customer_id
		client_token = braintree.ClientToken.generate({
				"customer_id": merchant_customer_id
			})
		if request.method == "POST":
			nonce = request.POST.get("payment_method_nonce", None)
			if nonce is None:
				messages.error(request, "An error occured please try again")
				return redirect("account_upgrade")
			if nonce is not None:
				payment_method_result = braintree.PaymentMethod.create({
						"customer_id": merchant_customer_id,
						"payment_method_nonce": nonce,
						"options":{
							"make_default": True
						}
					})
				if not payment_method_result.is_success:
					messages.error(request, "An error occured: %s" %(payment_method_result.message))
					return redirect("account_upgrade")

				the_token = payment_method_result.payment_method.token
				current_sub_id = merchant_obj.subscription_id
				current_plan_id = merchant_obj.plan_id
				did_create_sub = False
				did_update_sub = False
				trans_success = False
				trans_timestamp = None

				try:
					current_subscription = braintree.Subscription.find(current_sub_id)
					sub_status = current_subscription.status
				except:
					current_subscription = None
					sub_status = None 

				if current_subscription and sub_status == "Active":
					update_sub = braintree.Subscription.update(current_sub_id, {
							"payment_method_token": the_token,
						})
					did_update_sub = True
				else:
					create_sub = braintree.Subscription.create({
							"payment_method_token": the_token,
							"plan_id": PLAN_ID
						})
					did_create_sub = True

				if did_create_sub or did_update_sub:	
					membership_instance, created = Membership.objects.get_or_create(user=request.user)
					
					# messages.success(request, "Welcome to Woran. Your membership has been activated")


				if did_update_sub and not did_create_sub:
					messages.success(request, "Your plan has been updated")
					membership_dates_update.send(membership_instance, new_date_start=timezone.now())
					return redirect("account_home")


				elif did_create_sub and not did_update_sub:
					merchant_obj.subscription_id = create_sub.subscription.id 
					merchant_obj.plan_id = PLAN_ID
					merchant_obj.save()

					bt_tran = create_sub.subscription.transactions[0]
					new_tran, created = get_or_create_model_transaction(request.user, bt_tran)
					trans_success =False
					trans_timestamp = None
					if created:
						trans_timestamp = new_tran.timestamp
						trans_success = new_tran.success

					membership_dates_update.send(membership_instance, new_date_start=trans_timestamp)
					messages.success(request, "Welcome to Woran. Do enjoy your stay")
					return redirect("account_home")
				else:
					messages.error(request, "An error occured please try again")
					return redirect("account_upgrade")

		template = "billing/upgrade.html"
		context = {"client_token":client_token}
	return render(request, template, context)