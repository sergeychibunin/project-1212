from django.contrib import admin
from core.models import Page, ContentAudio, ContentText, ContentVideo


class PageAdmin(admin.ModelAdmin):
    search_fields = ['title']
    autocomplete_fields = ['videos', 'texts', 'audios']


class ContentAudioAdmin(admin.ModelAdmin):
    search_fields = ['title']


class ContentTextAdmin(admin.ModelAdmin):
    search_fields = ['title']


class ContentVideoAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(ContentVideo, ContentVideoAdmin)
admin.site.register(ContentText, ContentTextAdmin)
admin.site.register(ContentAudio, ContentAudioAdmin)
admin.site.register(Page, PageAdmin)
