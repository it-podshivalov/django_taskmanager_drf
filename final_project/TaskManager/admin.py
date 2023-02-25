from django.contrib import admin
from TaskManager.models import Project, Task, Status


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "Name",
        "Description",
        "Author",
    ]
    search_fields = [("Name")]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "Name",
        "Description",
        "Project",
        "CreationTime",
        "DeadlineForCompleting",
        "CompletionTime",
        "Executor",
        "Author",
        "Status",
    ]
    search_fields = [("Name")]

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'Name',
        # 'parent_status',
    ]

