from django.contrib import admin
from django.urls import path, include
from TaskManager.views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    ProjectUpdateView,
    ProjectCreateView,
    ProjectDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskListView.as_view(), name='tasks'),
    path("task/<slug:pk>/", TaskDetailView.as_view(), name="task"),
    path("task/update/<slug:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("task/delete/<slug:pk>/", TaskDeleteView.as_view(), name="task_delete"),
    path("create/", TaskCreateView.as_view(), name='task_create'),
    path('project/update/<slug:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path("project/delete/<slug:pk>/", ProjectDeleteView.as_view(), name="project_delete"),
    path('api/', include('TaskManager.urls')),
]
