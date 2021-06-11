from django.contrib import admin

# Register your models here.
from billing_details.models import billing,Salary
admin.site.register(billing)
admin.site.register(Salary)
