# Generated by Django 5.0.3 on 2024-05-07 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_is_task_task_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
    ]
