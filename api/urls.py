from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import RoomViewSet, OwnerViewSet, EventViewSet, EventAllViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('rooms', RoomViewSet)
router.register('owners', OwnerViewSet)
router.register('events', EventViewSet)
router.register('allevents', EventAllViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]