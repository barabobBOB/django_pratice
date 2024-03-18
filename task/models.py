from django.db import models


class TaskGroup(models.Model):
    """
    user_id는 유저 ID(PK) 입니다.
    복잡도를 줄이기 위해 외래키로 지정하지 않았습니다.
    """
    name = models.CharField(max_length=50)
    memo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    user_id = models.IntegerField()


class Task(models.Model):
    name = models.CharField(max_length=30)
    clear = models.IntegerField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    task_group_id = models.ForeignKey(
        TaskGroup,
        on_delete=models.CASCADE,
    )
