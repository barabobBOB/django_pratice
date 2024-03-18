from rest_framework import serializers

from task.models import TaskGroup


class TaskGroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(help_text="name")
    memo = serializers.CharField(help_text="memo")

    class Meta:
        model = TaskGroup
        fields = ['name', 'memo']
