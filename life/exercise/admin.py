from django.contrib import admin
from .models import Exercise, Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'date_created', 'duration')

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Exercise)
