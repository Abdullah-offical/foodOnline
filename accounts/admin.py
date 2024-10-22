from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'role', 'is_active')
    ordering = ('-date_joined',)
    list_filter = ()

    fieldsets = ()
    readonly_fields = ('last_login', 'date_joined')

    filter_horizontal = ()

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
