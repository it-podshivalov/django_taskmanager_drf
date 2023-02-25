from django.shortcuts import render
from rest_framework import viewsets, mixins
from django.contrib.admin.widgets import AdminDateWidget
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .models import Task, Status, Project
from django.contrib import messages
from .serializers import TaskSerializer
from .filters import TaskFilterSet, TaskFilter
from django_filters.views import FilterView


class TaskListView(FilterView):
    context_object_name = "tasks"
    model = Task
    queryset = Task.objects.all()
    template_name = "tasks_list.html"
    filter_class = TaskFilter

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = context['tasks']
        if self.filter_class:
            qs = self.filter_class(self.request.GET, queryset=qs).qs
        context['tasks'] = qs
        context['projects'] = Project.objects.all()
        return context


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "task_detail_view.html"


class TaskCreateView(CreateView):
    model = Task
    fields = ["Name", "Description", "DeadlineForCompleting", "Project", "Executor"]
    template_name = "task_create_view.html"

    def get_form(self, form_class=None):
        form = super(TaskCreateView, self).get_form(form_class)
        form.fields['DeadlineForCompleting'].widget = AdminDateWidget(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        form.instance.Author = self.request.user
        form.instance.Status = Status.objects.get(Name='Assigned')
        messages.success(self.request, "The task was created successfully.")
        return super(TaskCreateView, self).form_valid(form)

class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = "/"
    template_name = "task_delete_view.html"

class TaskUpdateView(UpdateView):
    model = Task
    fields = ["Name", "Description", "DeadlineForCompleting", "Project", "Executor", "Status"]
    template_name = "task_update_view.html"
    success_url = "/"
    queryset = Task.objects.all()

    def get_form(self, form_class=None):
        form = super(TaskUpdateView, self).get_form(form_class)
        form.fields['DeadlineForCompleting'].widget = AdminDateWidget(attrs={'type': 'date'})
        return form         


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ["Name", 'Description']
    template_name = "project_update_view.html"
    success_url = "/"
    queryset = Project.objects.all()

class ProjectCreateView(CreateView):
    model = Project
    fields = ["Name", "Description"]
    template_name = "project_create_view.html"
    success_url='/'

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super(ProjectCreateView, self).form_valid(form)

class ProjectDeleteView(DeleteView):
    model = Project
    context_object_name = "project"
    success_url = "/"
    template_name = "project_delete_view.html"        



class TaskViewSet(
    mixins.ListModelMixin, # GET /articles
    mixins.CreateModelMixin, # POST /articles
    mixins.RetrieveModelMixin, # GET /articles/1
    mixins.DestroyModelMixin, # DELETE /articles/1
    mixins.UpdateModelMixin, # PUT /articles/1
    viewsets.GenericViewSet
    ):           

    queryset = Task.objects.all().order_by("id")
    serializer_class = TaskSerializer
    filterset_class =  TaskFilterSet
