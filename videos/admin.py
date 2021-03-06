from django.contrib import admin
from .models import Video

# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'embed', 'screenshot', 'trailer', 'mediatype', 'partner')
    order_by = ('title',)
    search_fields = ('title',)
