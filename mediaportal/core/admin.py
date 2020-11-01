from django.contrib import admin
from core.models import Page, ContentAudio, ContentText, ContentVideo


admin.site.register(ContentVideo)
admin.site.register(ContentText)
admin.site.register(ContentAudio)
admin.site.register(Page)
