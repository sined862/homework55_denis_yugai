from django.contrib import admin
from tasks.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'date_deadline')
    list_filter = ('id', 'description', 'detail_description', 'status', 'date_deadline')
    search_fields = ('description', 'detail_description', 'status', 'date_deadline')
    fields = ('description', 'detail_description', 'status', 'date_deadline')


admin.site.register(Task, TaskAdmin)
