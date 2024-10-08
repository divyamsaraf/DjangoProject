from django.contrib import admin
from .models import UserDetails

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    
admin.site.register(UserDetails, UserDetailsAdmin)