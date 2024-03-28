from rest_framework import serializers

from task.models import TaskGroup, Task


class TaskGroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(help_text="name")
    memo = serializers.CharField(help_text="memo")

    class Meta:
        model = TaskGroup
        fields = ['name', 'memo']

class TaskSerializer(serializers.ModelSerializer):
    name = serializers.CharField(help_text="name")
    date = serializers.DateTimeField(help_text="date")
    task_group_id = serializers.PrimaryKeyRelatedField(queryset=TaskGroup.objects.all(), help_text="task_group_id")

    class Meta:
        model = Task
        fields = ['name', 'date', 'task_group_id']
