from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from task.views import TaskGroupList, TaskGroupDetail

urlpatterns = [
    path("group/", TaskGroupList.as_view()),
    path("group/<int:pk>/", TaskGroupDetail.as_view()),
]
