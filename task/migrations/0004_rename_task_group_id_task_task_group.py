# Generated by Django 5.0.3 on 2024-03-28 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_clear'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_group_id',
            new_name='task_group',
        ),
    ]