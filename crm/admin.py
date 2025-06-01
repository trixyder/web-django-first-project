from django.contrib import admin
from .models import Order, CrmStatus, CrmComment
# Register your models here.
admin.site.register(Order)
admin.site.register(CrmStatus)
admin.site.register(CrmComment)
