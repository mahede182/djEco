from django.contrib import admin
from .models import SiteSettings

class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'logo']
    
    def has_add_permission(self, request):
        # Prevent creating multiple settings instances
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deleting the settings instance
        return False

admin.site.register(SiteSettings, SiteSettingsAdmin)