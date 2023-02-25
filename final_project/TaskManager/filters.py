import django_filters
from django_filters import rest_framework as dj_filters
from .models import Task, Project, Status
from django.db.models import Q


class TaskFilterSet(dj_filters.FilterSet):
    """Набор фильров для представления для модели статей."""

    Project = dj_filters.CharFilter(field_name="Project", lookup_expr="icontains")

    class Meta:
        model = Task
        fields = [
            "Project",
        ]

class TaskFilter(django_filters.FilterSet):
    
    class Meta:
        model = Task
        fields = ['Name',]
     