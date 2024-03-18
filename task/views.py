from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from task.models import TaskGroup
from user.models import User
from task.serializers import TaskGroupSerializer


class TaskGroupList(APIView):
    permission_classes = [IsAuthenticated]

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
        task_groups = TaskGroup.objects.all()
        serializer = TaskGroupSerializer(task_groups, many=True)
        return Response(serializer.data)


class TaskGroupDetail(APIView):
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
