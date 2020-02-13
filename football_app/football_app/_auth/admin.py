from django.contrib import admin
from football_app._auth.models import MyUser

# Register your models here.


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')