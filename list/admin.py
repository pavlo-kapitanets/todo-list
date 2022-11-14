from django.contrib import admin

from list.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["description", "creation_date", "deadline_date", "completion", ]
    list_filter = ["creation_date"]
    search_fields = ["description"]