from django.db import models


class TaskGroup(models.Model):
    name = models.CharField(max_length=50)
    memo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class Task(models.Model):
    name = models.CharField(max_length=30)
    clear = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
