from rest_framework import serializers

from .models import ( 
    Notification,
)
from django.contrib.auth.models import User
from .tasks import send_notifications
from django.contrib.auth.models import User


class NotificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notification
        fields = (
            "id", "title", "body", "time_to_send", "conditional_clause", 
            "total_number", "completed_number",
        )
        read_only_fields = ("total_number", "completed_number",)
    
    def create(self, validated_data):
        time_to_send = validated_data.get("time_to_send", "")
        title = validated_data.get("title", "")
        body = validated_data.get("body", "")
        messge = {
            "title": title,
            "body": body
        }
        user_list = User.objects.values('id', 'username')
        validated_data["total_number"] = len(user_list)
        instance = super(NotificationSerializer, self).create(validated_data)
        messge["id"] = instance.id
        send_notifications(time_to_send, messge, user_list)
        return instance