from django.contrib import admin
from .models import *
from django.utils.html import mark_safe


@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_display_links = ('title', 'date')
    search_fields = ['title', 'date']

admin.site.register(HomeBG)
admin.site.register(OurService)
admin.site.register(ServiceIcons)
admin.site.register(AboutUs)
admin.site.register(ContactTxt)

@admin.register(OurGallery)
class OurGelleryModelAdmin(admin.ModelAdmin):
    list_display = ['title',  'img_preview']
    list_display_links = ['title']
    search_fields = ['title']
    readonly_fields = ['img_preview']

@admin.register(ContactUs)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name', 'email')
    search_fields = ['id', 'name', 'email']










