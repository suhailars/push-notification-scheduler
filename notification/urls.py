from django.conf.urls import include, url
from .views import (
	NotificationList,
)


urlpatterns = [
    url(r'^$', NotificationList.as_view()),
]