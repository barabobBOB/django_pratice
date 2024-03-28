from django.urls import path
from task.views import *

urlpatterns = [
    path("group/", TaskGroupListView.as_view(), name='taskgroup-list'),
    path("group/<int:pk>/", TaskGroupDetailView.as_view(), name='taskgroup-detail'),
    path("", TaskListView.as_view(), name='task-list-view'),
    path("<int:pk>/", TaskDetailView.as_view(), name='task-detail-view')
]

