from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','description',)

    def description(self, obj):
        return obj.description

    def occupation(self, obj):
        return obj.occupation

    def image(self, obj):
        return obj.image


admin.site.register(UserProfile, UserProfileAdmin)

