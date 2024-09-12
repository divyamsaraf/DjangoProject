from django.contrib import admin
from .models import UserDetails

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    
admin.site.register(UserDetails, UserDetailsAdmin)