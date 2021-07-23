from django.contrib import admin

from customer_info.models import UserProfileInfo, Customer, Account_detail
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Customer)
admin.site.register(Account_detail)
