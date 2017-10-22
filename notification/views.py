import json
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import Http404

from .serializers import (
    NotificationSerializer,
)
from .models import ( 
    Notification,
)


class NotificationList(APIView):
    """
    Register a new user.
    """
    serializer_class = NotificationSerializer
    #permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response({"id":data["id"]}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
