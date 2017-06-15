from django.contrib import admin

from .models import Membership, Transaction

admin.site.register(Membership)
admin.site.register(Transaction)