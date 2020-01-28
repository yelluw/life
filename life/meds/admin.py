from django.contrib import admin
from .models import Medication, Usage

class MedicationAdmin(admin.ModelAdmin):
    pass

class UsageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Medication, MedicationAdmin)
admin.site.register(Usage, UsageAdmin)

