from django.db import models

# Create your models here.
from django.db import models
from authentication.models import User

class Meeting(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organized_meetings")
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="meetings")
    scheduled_time = models.DateTimeField()
    topic = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
