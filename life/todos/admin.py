from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_filter = (
            'done',
            'date_due',
            'user',
            'date_created',
            )


admin.site.register(Todo, TodoAdmin)

