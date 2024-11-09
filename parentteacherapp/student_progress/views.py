from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import StudentProgress
from .serializers import StudentProgressSerializer
from rest_framework.permissions import IsAuthenticated

class StudentProgressViewSet(viewsets.ModelViewSet):
    queryset = StudentProgress.objects.all().order_by('-date')
    serializer_class = StudentProgressSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(updated_by=self.request.user)
