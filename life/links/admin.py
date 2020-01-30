from django.contrib import admin
from django.utils.html import format_html
from .models import Link, LinkGroup

class LinkAdmin(admin.ModelAdmin):
    list_display = ['clickable_link',]

    def clickable_link(self, obj):
        return format_html('<a href="{url}" target="_blank">{title}</a>', url=obj.url, title=obj.title) 

    clickable_link.short_description = 'Link'


admin.site.register(Link, LinkAdmin)
admin.site.register(LinkGroup)
