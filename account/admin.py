from django.contrib import admin
from account.models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob', 'address','phone_number', 'email',)
    list_filter = ('first_name', 'last_name', 'dob', 'address','phone_number', 'email',)
    search_fields = ['first_name', 'last_name', 'dob', 'address','phone_number', 'email',]
