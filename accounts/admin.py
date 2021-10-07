from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from accounts.form import UserForm
from accounts.models import User, Profile, UserAddress


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    list_display = ['name', 'profile_img', 'last_login', 'date_joined']
    add_fieldsets = (None, {
        'fields': (
            'name', 'email', 'password', 'password2',
            'is_active', 'is_staff', 'is_superuser'),
    }),


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'profile_img', 'user_email', 'user_last_login', 'user_join']


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    pass
