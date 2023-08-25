from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html
from django.conf import settings
from pathlib import Path

class AdvertisementAdmin(admin.ModelAdmin):

    @admin.display
    def image_tag(self, obj):
        if obj.image:
            print(obj.image.url)
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        else:
            default_image = settings.MEDIA_URL + "advertisements/image.png"
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', default_image)


    list_display = ["id", 'title', 'description', 'price', 'create_at', 'update_at', 'auction', 'image_tag']
    list_filter = ['auction', 'create_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image'),
        }),
        ('Финансы', {
            'fields': ("price", 'auction'),
            'classes': ['collapse']
        })
    )


    image_tag.short_description = 'Изображение'

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)
