from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

class UserAdmin(DefaultUserAdmin):
    list_display = DefaultUserAdmin.list_display + ('score',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Extra fields'), {'fields': ('score',)}), # include this
    )

# admin.site.unregister(User)
admin.site.register(User, UserAdmin)

