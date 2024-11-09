from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Meeting
from .serializers import MeetingSerializer
from rest_framework.permissions import IsAuthenticated

class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all().order_by('scheduled_time')
    serializer_class = MeetingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)
