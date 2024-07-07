from celery import shared_task
from django.core.mail import send_mail
from .models import Task

@shared_task
def send_task_reminder(task_id):
    task = Task.objects.get(id=task_id)
    send_mail(
        'Task Reminder',
        f'Remember to complete the task: {task.title}',
        'from@example.com',
        [task.member.user.email],
    )

