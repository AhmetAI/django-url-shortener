from django.contrib import admin
from .models import Url

class URLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_url_slug', 'date_created')
    search_fields = ('original_url', 'short_url_slug')
    list_filter = ('date_created',)

admin.site.register(Url, URLAdmin)
