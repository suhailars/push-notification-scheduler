# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import group
from celery.signals import task_success
from notification.models import Notification
from django.db.models import F


@shared_task
def send(user, message):
    print "sending mesage", message
    return message["id"]

def send_notifications(time_to_send, message, user_list):
    jobs = group(send.s(user, message) for user in user_list)
    result = jobs.apply_async(eta=time_to_send)
    return result 

@task_success.connect(sender=send)
def updated_notification(sender, **kwargs):
    id_ = kwargs.get("result", None)
    if id_:
        Notification.objects.filter(id=id_).update(completed_number=F('completed_number')+1)
    print "task_success", kwargs["result"]