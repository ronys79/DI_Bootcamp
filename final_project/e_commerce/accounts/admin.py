from django.contrib import admin
from .models import Account
from django.contrib.admin import ModelAdmin

# # configure admin and custom user model for admin panel 
# + model admin makes password read only
class AccountAdmin(ModelAdmin):
# what fields to display on admin panel for quick reference
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'phone_number', 'is_active')
# make fields a link to enter profile clicked
    list_display_links = ('email', 'first_name', 'last_name')
# makes fields read only + if wish not to show password delete from fields below to hide
    readonly_fields = ('last_login', 'date_joined', 'password')
    ordering = ('-date_joined',)


# tweeking admin site display/title
admin.site.site_header = 'Verde Vivero Website Admintration'
admin.site.index_title = 'Admin HomePage'
admin.site.site_title = 'Verde Vivero'

admin.site.register(Account, AccountAdmin)
