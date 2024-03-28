from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

import task
from task.models import TaskGroup, Task
from util.pagination import PaginationHandlerMixin
from user.models import User
from task.serializers import TaskGroupSerializer, TaskSerializer


class TaskGroupPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class TaskPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class TaskGroupListView(APIView, PaginationHandlerMixin):
    permission_classes = [IsAuthenticated]

    pagination_class = TaskGroupPagination
    serializer_class = TaskGroupSerializer

    @swagger_auto_schema(
        request_body=TaskGroupSerializer
    )
    def post(self, request):
        serializer = TaskGroupSerializer(data=request.data)
        user_id = User.objects.get(email=request.user.email).id
        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        task_groups = TaskGroup.objects.order_by('-created_at')
        page = self.paginate_queryset(task_groups)

        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(task_groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskGroupDetailView(APIView):
    def get_object(self, pk):
        try:
            return TaskGroup.objects.get(id=pk)
        except TaskGroup.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task_group = self.get_object(pk)
        serializer = TaskGroupSerializer(task_group)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=TaskGroupSerializer
    )
    def put(self, request, pk, format=None):
        task_group = self.get_object(pk)
        serializer = TaskGroupSerializer(task_group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task_group = self.get_object(pk)
        task_group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskListView(APIView, PaginationHandlerMixin):
    permission_classes = [IsAuthenticated]

    pagination_class = TaskPagination
    serializer_class = TaskSerializer

    @swagger_auto_schema(
        request_body=TaskSerializer
    )
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        tasks = Task.objects.order_by('-created_at')
        page = self.paginate_queryset(tasks)

        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_object(self, pk):
        try:
            return Task.objects.get(id=pk)
        except Task.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        request_body=TaskSerializer
    )
    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)