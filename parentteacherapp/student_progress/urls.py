from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentProgressViewSet

router = DefaultRouter()
router.register('progress', StudentProgressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
