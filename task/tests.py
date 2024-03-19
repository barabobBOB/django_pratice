from django.test import TestCase
from rest_framework.test import APIClient
from task.models import TaskGroup
from rest_framework import status
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model

from task.serializers import TaskGroupSerializer


class TaskGroupListTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(email='test@example.com', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # TaskGroup 객체 생성
        self.url = reverse('taskgroup-list')
        TaskGroup.objects.create(name='group', memo='memo', user_id=self.user.pk)

    def test_create_taskgroup(self):
        data = {
            'name': 'group',
            'memo': 'memo'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TaskGroup.objects.count(), 2)
        self.assertEqual(TaskGroup.objects.latest('id').name, 'group')
        self.assertEqual(TaskGroup.objects.latest('id').memo, 'memo')

    def test_get_taskgroup_list(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'group')
        self.assertEqual(response.data[0]['memo'], 'memo')


class TaskGroupDetailTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(email='test@example.com', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # TaskGroup 객체 생성
        self.task_group = TaskGroup.objects.create(name='group', memo='memo', user_id=self.user.id)
        self.url = reverse('taskgroup-detail', kwargs={'pk': self.task_group.pk})

    def test_get_taskgroup(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = TaskGroupSerializer(self.task_group).data
        self.assertEqual(response.data, expected_data)

    def test_update_taskgroup(self):
        updated_data = {'name': 'group2', 'memo': 'memo2', 'user_id': self.user.id}
        response = self.client.put(self.url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task_group.refresh_from_db()
        self.assertEqual(self.task_group.name, 'group2')
        self.assertEqual(self.task_group.memo, 'memo2')

    def test_delete_taskgroup(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(TaskGroup.DoesNotExist):
            TaskGroup.objects.get(pk=self.task_group.pk)
