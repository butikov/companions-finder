from django.contrib import admin
from .models import DefaultUser
# Register your models here.


@admin.register(DefaultUser)
class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'first_name', 'last_name')
