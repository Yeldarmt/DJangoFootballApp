from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from football_app._auth.models import MyUser, Notification


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'address')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )

admin.site.register(Notification)