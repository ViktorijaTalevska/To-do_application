from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):

    list_display = ["id", "user", "title", "godini", "completed", "created_at", "updated_at"]
    list_filter = ["completed", "created_at"]

    admin.site.register(Task)