from django.urls import path
from task.views import TaskGroupList, TaskGroupDetail

urlpatterns = [
    path("group/", TaskGroupList.as_view(), name='taskgroup-list'),
    path("group/<int:pk>/", TaskGroupDetail.as_view(), name='taskgroup-detail'),
]
